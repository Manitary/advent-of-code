F:=Open("input5.txt","r");
poly:=Eltseq(Gets(F));

procedure react(~poly,i,c)
	if i le #poly and StringToCode(StringToLower(poly[i])) eq c then
		Remove(~poly,i);
		react(~poly,i,c);
	elif i lt #poly then
		if Abs(StringToCode(poly[i])-StringToCode(poly[i+1])) eq 32 then
			Remove(~poly,i);
			Remove(~poly,i);
			if i eq 1 then
				react(~poly,1,c);
			else
				react(~poly,i-1,c);
			end if;
		else
			react(~poly,i+1,c);
		end if;
	end if;
end procedure;

//Magma gives a segmentation fault when using react on the original string, so I had to split it into smaller pieces :[

function splitopt(poly,n,c);
	polysplit:=[[poly[i]:i in [(#poly div n)*j+1..(#poly div n)*(j+1)]]:j in [0..n-1]];
	for i in [1..n] do
		react(~polysplit[i],1,c);
	end for;
	polymerge:=&cat(polysplit);
	react(~polymerge,1,c);
	return polymerge;
end function;

poly:=splitopt(poly,5,0);

PrintFile("day05.txt",#poly);
PrintFile("day05.txt",Min([#splitopt(poly,5,i):i in [97..122]]));
