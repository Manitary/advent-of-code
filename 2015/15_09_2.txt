input:=[["Tristram","AlphaCentauri","34"],["Tristram","Snowdin","100"],["Tristram","Tambi","63"],["Tristram","Faerun","108"],["Tristram","Norrath","111"],["Tristram","Straylight","89"],["Tristram","Arbre","132"],["AlphaCentauri","Snowdin","4"],["AlphaCentauri","Tambi","79"],["AlphaCentauri","Faerun","44"],["AlphaCentauri","Norrath","147"],["AlphaCentauri","Straylight","133"],["AlphaCentauri","Arbre","74"],["Snowdin","Tambi","105"],["Snowdin","Faerun","95"],["Snowdin","Norrath","48"],["Snowdin","Straylight","88"],["Snowdin","Arbre","7"],["Tambi","Faerun","68"],["Tambi","Norrath","134"],["Tambi","Straylight","107"],["Tambi","Arbre","40"],["Faerun","Norrath","11"],["Faerun","Straylight","66"],["Faerun","Arbre","144"],["Norrath","Straylight","115"],["Norrath","Arbre","135"],["Straylight","Arbre","127"]];

cities:={};
for item in input do
	Include(~cities,item[1]);
	Include(~cities,item[2]);
end for;
max_dist:=0;

for order in Permutations(cities) do
	dist:=0;
	for i in [1..#order-1] do
		pair:={order[i],order[i+1]};
		for item in input do
			if item[1] in pair and item[2] in pair then
				dist+:=StringToInteger(item[3]);
				break;
			end if;
		end for;
	end for;
	if dist gt max_dist then
		max_dist:=dist;
	end if;
end for;
max_dist;