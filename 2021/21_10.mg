F:=Open("input10.txt","r");

input:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~input, s);
end while;

opener:=["(","[","{","<"];
closer:=[")","]","}",">"];
point_corruption:=[3, 57, 1197, 25137];
point_completion:=[1, 2, 3, 4];
point_mult:=5;

score_corruption:=0;
score_completion:=[];

for line in input do
	check:=[];
	corrupted:=false;
	for i in [1..#line] do
		if line[i] in opener then
			Append(~check, line[i]);
		else
			if Index(closer, line[i]) eq Index(opener, check[#check]) then
				Remove(~check, #check);
			else
				score_corruption +:= point_corruption[Index(closer, line[i])];
				corrupted:=true;
				break;
			end if;
		end if;
	end for;
	if not corrupted and #check ne 0 then
		//check;
		score_line:=0;
		for c in Reverse(check) do
			score_line *:= point_mult;
			score_line +:= point_completion[Index(opener, c)];
		end for;
		Append(~score_completion, score_line);
	end if;
end for;

PrintFile("day10.txt", score_corruption);

Sort(~score_completion);

PrintFile("day10.txt", score_completion[(#score_completion div 2) + 1]);
