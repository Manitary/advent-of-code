F:=Open("input5.txt","r");
poly:=Prune(Eltseq(Gets(F)));
F:=FreeGroup(26);

/*
If Magma didn't give a segmentation fault (string too long?) I would use this:

word:="";
for c in poly do
	num:=StringToCode(c) le 90 select IntegerToString(StringToCode(c)-64) else IntegerToString(StringToCode(c)-96)*"^-1";
	word*:="F."*num*"*";
end for;
word:=Substring(word,1,#word-1);

word:=eval word;

Instead, we have to split the string first and then merge the reductions.
*/

n:=5;
polysplit:=[[poly[i]:i in [(#poly div n)*j+1..(#poly div n)*(j+1)]]:j in [0..n-1]];
words:=[];

for poly in polysplit do
	word:="";
	for c in poly do
		num:=StringToCode(c) le 90 select IntegerToString(StringToCode(c)-64) else IntegerToString(StringToCode(c)-96)*"^-1";
		word*:="F."*num*"*";
	end for;
	word:=Substring(word,1,#word-1);
	Append(~words,word);
end for;

word:=&*[eval words[i]:i in [1..n]];

PrintFile("day05.txt",#word);
reductions:=[];
for i in [1..26] do
	Append(~reductions,#Eliminate(word,F.i,Id(F)));
end for;
PrintFile("day05.txt",Min(reductions));
