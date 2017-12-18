input:=344;

function module(input,n)
	if input mod n eq 0 then
		return n;
	else
		return input mod n;
	end if;
end function;

buffer_size:=1;
position:=0;

for i in [1..50000000] do
	position:=module(position+input,buffer_size);
	if position eq 1 then
		result:=i;
	end if;
	buffer_size+:=1;
	position:=module(position+1,buffer_size);
end for;

result;
	