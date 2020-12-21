//incomplete
F:=Open("input19.txt","r");

rules:=AssociativeArray();
input:=[];

while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	p:=Index(s,":");
	if p gt 0 then
		n:=Substring(s,1,p-1);
		r:=Substring(s,p+2,#s-p-1);
		if "\"" in r then
			rules[n]:=r[2];
		else
			rules[n]:="("*r*")";
		end if;
		/*
		if "|" in r then
			rules[n]:="("*r*")";
		elif "\"" in r then
			rules[n]:=r[2];
		else
			rules[n]:=r;
		end if;
		*/
	elif #s gt 0 then
		Append(~input,s);
	end if;
end while;

function printlist(array)
	for k in Sort(SetToSequence(Keys(array))) do 
		print array[k];
	end for;
	return true;
end function;

function IsDigit(char)
	return StringToCode(char) in [48..57];
end function;

function NumReplace(string,match,new)
	l:=#match;
	b, w, _:=Regexp("(^|[^0-9])"*match*"($|[^0-9])",string);
	if b then
		p:=Index(string,match);
		while (p+l le #string and IsDigit(string[p+l])) or (p gt 1 and IsDigit(string[p-1])) do
			s1:=Eltseq(string);
			p+:=1;
			p:=Index(s1,match,p);
		end while;
		return (
			(p gt 1 select Substring(string,1,p-1) else "") * 
			new * 
			(p+l le #string select Substring(string,p+l,#string-p-l+1) else "")
			);
	else
		return string;
	end if;
end function;

keyss:=Sort(SetToSequence(Keys(rules)));
keys:=Keys(rules);
done:={};
rules1:=rules;

function check(i)
	return rules1[IntegerToString(i)];
end function;

repeat
	to_check:={x:x in keys diff done|not Regexp("[0-9]",rules[x])};
	done join:=to_check;
	to_check;
	for k in keys diff done do
		for i in done do
			rules[k]:=NumReplace(rules[k],i,rules[i]);
		end for;
	end for;
	done join:=to_check;
until done eq keys or to_check eq {};

rule:=Eltseq(rules["0"]);
while " " in rule do 
	Exclude(~rule," ");
end while;
rule:="^"*&*rule*"$";
rule;

for k in [IntegerToString(x):x in Sort([StringToInteger(y):y in keyss])] do PrintFileMagma("test.txt",k); PrintFileMagma("test.txt",rules[k]);  end for;
