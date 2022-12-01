F:=Open("input25.txt","r");
pubkey_card:=StringToInteger(Gets(F));
pubkey_door:=StringToInteger(Gets(F));

subject:=7;
step:=func<val,sub|(val*sub) mod 20201227>;
function loopcalc(sub,key)
	val:=1;
	count:=0;
	repeat
		count+:=1;
		val:=step(val,subject);	
	until val eq key;
	return count;
end function;

loopsize_card:=loopcalc(subject,pubkey_card);
//loopsize_door:=loopcalc(subject,pubkey_door);

n:=1;
for i in [1..loopsize_card] do
	n:=step(n,pubkey_door);
end for;
PrintFile("day25.txt",n);

/*
n:=1;
for i in [1..loopsize_door] do
	n:=step(n,pubkey_card);
end for;
print n
*/
