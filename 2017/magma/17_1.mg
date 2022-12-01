input:=344;

function module(input,n)
	if input mod n eq 0 then
		return n;
	else
		return input mod n;
	end if;
end function;

buffer:=[0];
position:=1;

for i in [1..2017] do
	position:=module(position+input,#buffer);
	Insert(~buffer,position+1,i);
	position:=module(position+1,#buffer);
end for;

buffer[position+1];
	