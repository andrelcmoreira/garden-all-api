DO
$$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_catalog.pg_roles
      WHERE rolname = 'garden_all'
   ) THEN
      CREATE ROLE garden_all LOGIN PASSWORD '5(046xu2[tGi';
   END IF;
END
$$;

GRANT CONNECT ON DATABASE garden_all_db TO garden_all;
