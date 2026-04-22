create or replace function get_pattern(
    pattern varchar
)
returns table(
    name varchar,
    phone varchar
)
as $$-
begin
    return query
    select c.name, c.phone from contacts c where c.name ilike '%' || pattern ||'%'
    or c.phone ilike '%' || pattern ||'%';
end;
$$ language plpgsql;



create or replace function query_pagination(
    page_number int,
    page_size int
)
returns table(
    name varchar,
    phone varchar
)
as $$
begin
    return query 
    select c.name, c.phone from contacts c limit page_size offset (page_number - 1) * page_size;
end;
$$ language plpgsql;
