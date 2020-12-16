F:=Open("input16.txt","r");

rules:=[];
tickets:=[];
t:=false;
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	if Regexp("ticket", s) then
		t:=true;
	end if;
	if t then
		if "," in s then
			Append(~tickets,[StringToInteger(x):x in Split(s,",")]);
		end if;
	else
		rule,_,range:=Regexp("(.+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)",s);
		if rule then
			Append(~rules, [*range[1],[StringToInteger(range[i]):i in [2..#range]]*]);
		end if;
	end if;
end while;

CheckRule:=func<rule, val|(val ge rule[1] and val le rule[2]) or (val ge rule[3] and val le rule[4])>;

function CheckTicket(rules, ticket)
	valid:=true;
	err:=0;
	for v in ticket do
		test:=&or[CheckRule(r[2],v):r in rules];
		if not test then
			err+:=v;
			valid:=false;
		end if;
	end for;
	return valid, err;
end function;

error_rate:=0;
i:=2;
while i le #tickets do
	valid, err:=CheckTicket(rules, tickets[i]);
	if valid then
		i+:=1;
	else
		error_rate+:=err;
		Remove(~tickets,i);
	end if;
end while;

PrintFile("day16.txt",error_rate);

candidates:=[];
for r in rules do
	Append(~candidates,[]);
	for j in [1..#tickets[1]] do
		if &and[CheckRule(r[2], t[j]):t in tickets] then
			Append(~candidates[#candidates],j);
		end if;
	end for;
end for;

order:=[];
while true do
	if exists(i){x:x in [1..#candidates]|#candidates[x] eq 1} then
		val:=candidates[i][1];
		order[i]:=val;
		for i in [1..#candidates] do
			Exclude(~candidates[i],val);
		end for;
		print order, candidates;
	else
		break;
	end if;
end while;

PrintFile("day16.txt",&*[tickets[1][i]:i in {order[j]:j in [1..6]}]);
