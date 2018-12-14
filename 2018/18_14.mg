F:=Open("input14.txt","r");
input:=StringToInteger(Gets(F));

nmod:=func<n,m|n mod m eq 0 select m else n mod m>;

procedure work(~score,~pos)
	new_score:=&+[score[p]:p in pos];
	score cat:=new_score eq 0 select [0] else Reverse(Intseq(new_score));
	for j in [1..#pos] do
		pos[j]:=nmod(pos[j]+score[pos[j]]+1,#score);
	end for;
end procedure;

score:=[3,7];
pos:=[1,2];
repeat
	work(~score,~pos);
until #score ge input+10;
PrintFile("day14.txt",&*[IntegerToString(score[input+c]):c in [1..10]]);

score:=[3,7];
pos:=[1,2];
l:=#IntegerToString(input);
pattern:=Reverse(Intseq(input));

repeat
	work(~score,~pos);
	if score eq pattern then
		PrintFile("day14.txt",0);
	end if;
until #score gt l and IsSubsequence(pattern,[score[c]:c in [#score-l..#score]]);

if pattern eq [score[c]:c in [#score-l+1..#score]] then
	PrintFile("day14.txt",#score-l);
else
	PrintFile("day14.txt",#score-l-1);
end if;
