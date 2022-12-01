F:=Open("input14.txt","r");

template:=Eltseq(Gets(F));
Gets(F);

rules:=AssociativeArray();
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	s:=Split(s, " ->");
	rules[s[1]]:=s[2];
end while;

pairs:=AssociativeArray();

procedure AddValue(~aa, k, n)
	aa[k]:=k in Keys(aa) select aa[k]+n else n;
end procedure;

for i in [1..#template-1] do
	pair:=template[i]*template[i+1];
	AddValue(~pairs, pair, 1);
end for;

for i in [1..40] do
	newpairs:=AssociativeArray();
	for p in Keys(pairs) do
		AddValue(~newpairs, p[1]*rules[p], pairs[p]);
		AddValue(~newpairs, rules[p]*p[2], pairs[p]);
	end for;
	pairs:=newpairs;
	if i in [10,40] then
		polymer:={*k[1]^^pairs[k]:k in Keys(pairs)*} join {*template[#template]*};
		mults:=[Multiplicity(polymer,x):x in MultisetToSet(polymer)];
		Max(mults)-Min(mults);
	end if;
end for;
