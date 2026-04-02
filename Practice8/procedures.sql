create or replace procedure insert_name_phone(
    p_name varchar,
    p_phone varchar
)
language plpgsql 
as $$
begin
    if exists(select 1 from contacts where name = p_name) then
        UPDATE contacts SET phone=p_phone where name=p_name;
    else
        INSERT INTO contacts(name,phone) VALUES(p_name,p_phone);
    end if;
end;
$$;

create or replace procedure insert_many(
    p_names varchar[],
    p_phones varchar[]
)
language plpgsql
as $$
declare
    i integer;
begin
    for i in 1..array_length(p_names,1) LOOP
        if p_phones[i] ~ '^\d{11}$' THEN
            INSERT INTO contacts(name,phone) VALUES(p_names[i],p_phones[i]);
        else    
            RAISE NOTICE 'Not valid phone: %', p_phones[i];
        END IF;
    END LOOP;
end;
$$;


create or replace procedure delete_by(
    p_name varchar,
    p_phone varchar
)
language plpgsql
as $$
begin
    DELETE from contacts where name=p_name or phone=p_phone;
    if NOT FOUND THEN
        RAISE NOTICE 'No such contact';
    END IF;
end;
$$;

  

