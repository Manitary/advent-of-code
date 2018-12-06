F:=Open("input5.txt","r");
poly:=Prune(Eltseq(Gets(F)));

word:="";
for c in poly do
	num:=StringToCode(c) le 90 select StringToCode(c)-64 else StringToCode(c)-70;
	num:=IntegerToString(num);
	word*:="F."*num*"*";
end for;
word:=Substring(word,1,#word-1);

G:=FreeGroup(52);
for i in [1..26] do
	G:=quo<G|G.i*G.(i+26),G.(i+26)*G.i>;
end for;
F:=RWSGroup(G);

PrintFile("day05.txt",#eval word);

word:=Sprint(eval word);
reductions:=[];
for i in [1..26] do
	F:=RWSGroup(quo<G|G.i>);
	Append(~reductions,#eval word);
end for;
PrintFile("day05.txt",Min(reductions));
