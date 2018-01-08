input:="1113122113";

procedure stuff(~string)
	s:="";
	repeat
		k:=string[1];
		i:=0;
		repeat
			i+:=1;
			if #string gt 1 then
				string:=Substring(string,2,#string-1);
			else
				string:="";
			end if;
		until #string eq 0 or string[1] ne k;
		s*:=IntegerToString(i);
		s*:=k;
	until #string eq 0;
	string:=s;
end procedure;

for n in [1..50] do
	stuff(~input);
end for;
#input;