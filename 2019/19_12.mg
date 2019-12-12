F:=Open("input12.txt","r");

input:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	s:=Split(s,",");
	Append(~input,[]);
	for c in s do
		_,coord:=Regexp("[-0-9]+",c);
		Append(~input[#input],StringToInteger(coord));
	end for;
end while;

function Gravity(m1,m2)
	return [m1[i] gt m2[i] select -1 else (m1[i] eq m2[i] select 0 else 1):i in [1..#m1]];
end function;

Energy:=func<m|&+[Abs(x):x in m]>;
TotalEnergy:=func<l1,l2,i|Energy(l1[i])*Energy(l2[i])>;

moons:=input;
velocity:=[[0,0,0]:m in moons];

for i in [1..1000] do
	for j in [1..#moons-1] do
		for k in [j+1..#moons] do
			v:=Gravity(moons[j],moons[k]);
			for l in [1..3] do
				velocity[j,l]+:=v[l];
				velocity[k,l]-:=v[l];
			end for;
		end for;
	end for;
	for j in [1..#moons] do
		for k in [1..3] do
			moons[j,k]+:=velocity[j,k];
		end for;
	end for;
end for;

PrintFile("day12.txt",&+[TotalEnergy(moons,velocity,i):i in [1..#moons]]);

moons:=input;
velocity:=[[0,0,0]:m in moons];
initial_states:=[[<m[i],v[i]>:m in moons,v in velocity]:i in [1..3]];
found:=[false:i in [1..3]];
periods:=[0:i in [1..3]];
count:=0;
repeat
	count+:=1;
	for j in [1..#moons-1] do
		for k in [j+1..#moons] do
			v:=Gravity(moons[j],moons[k]);
			for l in [1..3] do
				velocity[j,l]+:=v[l];
				velocity[k,l]-:=v[l];
			end for;
		end for;
	end for;
	for j in [1..#moons] do
		for k in [1..3] do
			moons[j,k]+:=velocity[j,k];
		end for;
	end for;
	new_states:=[[<m[i],v[i]>:m in moons,v in velocity]:i in [1..3]];
	for i in [1..3] do
		if not found[i] then
			if new_states[i] eq initial_states[i] then
				found[i]:=true;
				periods[i]:=count;
			end if;
		end if;
	end for;
until &and(found);

PrintFile("day12.txt",LCM(periods));
