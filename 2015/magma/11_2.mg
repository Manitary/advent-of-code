input:="hxbxwxba";

pass:=[];
for i in [1..#input] do
	Append(~pass,StringToCode(input[i]));
end for;
wrap:=false;

procedure update(~letter,~wrap)
	wrap:=false;
	letter+:=1;
	if letter eq 123 then
		letter:=97;
		wrap:=true;
	elif letter in {105, 108, 111} then
		letter+:=1;
	end if;
end procedure;
	
procedure increment(~pass)
	d:=#pass+1;
	repeat
		d-:=1;
		update(~pass[d],~wrap);
	until not(wrap);
end procedure;

function islegal(pass)
	seq:=false;
	pairs:=false;
	char:=true;
	for d in pass do
		if d in {105, 108, 111} then
			char:=false;
		end if;
	end for;
	for d in [1..#pass-2] do
		if pass[d]+1 eq pass[d+1] and pass[d]+2 eq pass[d+2] then
			seq:=true;
			break;
		end if;
	end for;
	for d in [1..#pass-3] do
		if pass[d] eq pass[d+1] then
			for e in [d+2..#pass-1] do
				if pass[e] eq pass[e+1] then
					pairs:=true;
					break d;
				end if;
			end for;
		end if;
	end for;
	return seq and pairs and char;
end function;

repeat
	increment(~pass);
until islegal(pass);
repeat
	increment(~pass);
until islegal(pass);

new_pass:="";
for c in pass do
	new_pass*:=CodeToString(c);
end for;
new_pass;