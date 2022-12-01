input:=[["Sugar","3","0","0","-3","2"],["Sprinkles","-3","3","0","0","9"],["Candy","-1","0","4","0","1"],["Chocolate","0","0","-2","2","8"]];
input:=[[StringToInteger(input[r][i]) : i in [2..#input[r]]] : r in [1..#input]];
max_score:=0;

partitions:={};
for seq in Partitions(100,#input) do
	for perm in Permutations({1..#input}) do
		Include(~partitions,[seq[i]:i in perm]);
	end for;
end for;

for seq in partitions do
	score:=1;
	prop:=[0: i in [1..#input[1]]];
	for i in [1..#input] do
		for p in [1..#input[1]] do
			prop[p]+:=input[i][p]*seq[i];
		end for;
	end for;
	if prop[#prop] ne 500 then
		score:=0;
	else
		for p in [1..#prop-1] do
			score*:=Maximum(prop[p],0);
		end for;
	end if;
	max_score:=Maximum(max_score,score);
end for;
max_score;