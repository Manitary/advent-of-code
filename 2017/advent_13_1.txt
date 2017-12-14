input:=[[0,4],[1,2],[2,3],[4,5],[6,8],[8,6],[10,4],[12,6],[14,6],[16,8],[18,8],[20,6],[22,8],[24,8],[26,8],[28,12],[30,12],[32,9],[34,14],[36,12],[38,12],[40,12],[42,12],[44,10],[46,12],[48,12],[50,10],[52,14],[56,12],[58,14],[62,14],[64,14],[66,12],[68,14],[70,14],[72,17],[74,14],[76,14],[80,20],[82,14],[90,24],[92,14],[98,14]];

for i in [1..#input] do
	Append(~input[i],1);
end for;
position:=-1;
severity:=0;

for t in [0..input[#input][1]] do
	position+:=1;
	if input[1][1] eq position then
		if input[1][3] eq 1 then
			severity+:=position*input[1][2];
		end if;
		Remove(~input,1);
	end if;
	for n in [1..#input] do
		if (t mod (input[n][2]-1)) eq (t mod ((input[n][2]-1)*2)) then
			input[n][3]+:=1;
		else
			input[n][3]-:=1;
		end if;
	end for;
end for;

severity;