input:=[["Alice","-2","Bob"],["Alice","-62","Carol"],["Alice","65","David"],["Alice","21","Eric"],["Alice","-81","Frank"],["Alice","-4","George"],["Alice","-80","Mallory"],["Bob","93","Alice"],["Bob","19","Carol"],["Bob","5","David"],["Bob","49","Eric"],["Bob","68","Frank"],["Bob","23","George"],["Bob","29","Mallory"],["Carol","-54","Alice"],["Carol","-70","Bob"],["Carol","-37","David"],["Carol","-46","Eric"],["Carol","33","Frank"],["Carol","-35","George"],["Carol","10","Mallory"],["David","43","Alice"],["David","-96","Bob"],["David","-53","Carol"],["David","-30","Eric"],["David","-12","Frank"],["David","75","George"],["David","-20","Mallory"],["Eric","8","Alice"],["Eric","-89","Bob"],["Eric","-69","Carol"],["Eric","-34","David"],["Eric","95","Frank"],["Eric","34","George"],["Eric","-99","Mallory"],["Frank","-97","Alice"],["Frank","6","Bob"],["Frank","-9","Carol"],["Frank","56","David"],["Frank","-17","Eric"],["Frank","18","George"],["Frank","-56","Mallory"],["George","45","Alice"],["George","76","Bob"],["George","63","Carol"],["George","54","David"],["George","54","Eric"],["George","30","Frank"],["George","7","Mallory"],["Mallory","31","Alice"],["Mallory","-32","Bob"],["Mallory","95","Carol"],["Mallory","91","David"],["Mallory","-66","Eric"],["Mallory","-75","Frank"],["Mallory","-99","George"]];

function module(n,m)
	if n mod m eq 0 then
		return m;
	else
		return n mod m;
	end if;
end function;

people:={};
for item in input do
	Include(~people,item[1]);
	Include(~people,item[3]);
end for;
max_happy:=0;

for order in Permutations(people) do
	happy:=0;
	for i in [1..#order] do
		pair:={order[i],order[module(i+1,#order)]};
		for item in input do
			if item[1] in pair and item[3] in pair then
				happy+:=StringToInteger(item[2]);
			end if;
		end for;
	end for;
	max_happy:=Maximum(happy,max_happy);
end for;
max_happy;

//not optimized, the cyclic symmetry makes Permutation(people) getting many duplicates