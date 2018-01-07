input:=[["Vixen","19","7","124"],["Rudolph","3","15","28"],["Donner","19","9","164"],["Blitzen","19","9","158"],["Comet","13","7","82"],["Cupid","25","6","145"],["Dasher","14","3","38"],["Dancer","3","16","37"],["Prancer","25","6","143"]];

input:=[[StringToInteger(input[r][i]) : i in [2..4]] : r in [1..#input]];
dist:=[0:i in [1..#input]];
t:=2503;

for r in [1..#input] do
	dist[r]+:=input[r][1]*(input[r][2]*(t div (input[r][2]+input[r][3]))+Minimum((t mod (input[r][2]+input[r][3])),input[r][2]));
end for;
m:=Maximum(dist);
m;