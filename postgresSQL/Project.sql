-- create database event_analytics;

-- #################################################

create schema analytics;


-- #################################################

-- TENANTS
CREATE TABLE analytics.tenants (
    tenant_id SERIAL PRIMARY KEY,
    tenant_name VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- USERS (tenant-scoped users)
CREATE TABLE analytics.users (
    user_id INT,
    tenant_id INT,
    user_name VARCHAR(50),
    email VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (tenant_id, user_id),
    FOREIGN KEY (tenant_id) REFERENCES analytics.tenants(tenant_id)
);

-- EVENTS (Partitioned)
CREATE TABLE analytics.events (
    event_id BIGSERIAL,
    tenant_id INT NOT NULL,
    user_id INT NOT NULL,
    event_name TEXT NOT NULL,
    event_time TIMESTAMP NOT NULL,
    properties JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (event_id, event_time),
    FOREIGN KEY (tenant_id, user_id)
        REFERENCES analytics.users(tenant_id, user_id)
) PARTITION BY RANGE (event_time);

-- #################################################

-- PARTITIONING

CREATE TABLE analytics.events_2026_01
PARTITION OF analytics.events
FOR VALUES FROM ('2026-01-01') TO ('2026-02-01');

CREATE TABLE analytics.events_2026_02
PARTITION OF analytics.events
FOR VALUES FROM ('2026-02-01') TO ('2026-03-01');

CREATE TABLE analytics.events_2026_03
PARTITION OF analytics.events
FOR VALUES FROM ('2026-03-01') TO ('2026-04-01');

CREATE TABLE analytics.events_2026_04
PARTITION OF analytics.events
FOR VALUES FROM ('2026-04-01') TO ('2026-05-01');

CREATE TABLE analytics.events_default
PARTITION OF analytics.events DEFAULT;


-- #################################################

-- 1. Tenant + Time 
CREATE INDEX idx_events_tenant_time
ON analytics.events (tenant_id, event_time);

-- 2. Event Name
CREATE INDEX idx_events_event_name
ON analytics.events (event_name);

-- 3. JSONB GIN Index
CREATE INDEX idx_events_properties
ON analytics.events USING GIN (properties);


-- #################################################

-- TRIGERS

CREATE OR REPLACE FUNCTION set_created_at()
RETURNS TRIGGER AS 
$$
BEGIN
    NEW.created_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_created_at
BEFORE INSERT ON analytics.events
FOR EACH ROW
EXECUTE FUNCTION set_created_at();




CREATE OR REPLACE FUNCTION validate_event()
RETURNS TRIGGER AS 
$$
BEGIN
    IF NEW.event_name IS NULL THEN
        RAISE EXCEPTION 'event_name cannot be null';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_validate_event
BEFORE INSERT ON analytics.events
FOR EACH ROW
EXECUTE FUNCTION validate_event();


-- #################################################



CREATE OR REPLACE FUNCTION bulk_insert_events(events JSONB)
RETURNS VOID AS 
$$
DECLARE
    rec JSONB;
BEGIN
    FOR rec IN SELECT * FROM jsonb_array_elements(events)
    LOOP
        INSERT INTO analytics.events (tenant_id, user_id, event_name, event_time, properties)
        VALUES (
            rec->>'tenant_id',
            rec->>'user_id',
            rec->>'event_name',
            (rec->>'event_time')::timestamp,
            rec->'properties'
        );
    END LOOP;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION delete_old_events()
RETURNS VOID AS 
$$
BEGIN
    DELETE FROM analytics.events
    WHERE event_time < NOW() - INTERVAL '90 days';
END;
$$ LANGUAGE plpgsql;




-- #################################################


create materialized view analytics.dau_mv as 
select 
tenant_id,date(event_time) as even_date,
count (distinct user_id) as dau
from analytics.events
group by tenant_id,date(event_time);

create materialized view analytics.revenue_mv as
select 
tenant_id,date(event_time) as event_date,
sum((properties->>'amount')::int) as revenue
from analytics.events
where event_name='purchase'
group by tenant_id,date(event_time);


create unique index dav_mv_idx
on analytics.dau_mv(tenant_id,even_date);


create unique index revenue_mv_idx
on analytics.revenue_mv (tenant_id,event_date);


REFRESH MATERIALIZED VIEW CONCURRENTLY analytics.dau_mv;
REFRESH MATERIALIZED VIEW CONCURRENTLY analytics.revenue_mv;


