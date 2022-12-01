F:=Open("input4.txt","r");
batch:=[];
while true do
	entry:="";
	repeat
		s:=Gets(F);
		if IsEof(s) then
			break;
		end if;
		if #s gt 0 then
			if #entry gt 0 then
				entry*:=" ";
			end if;
			entry*:=s;
		end if;
	until #s eq 0; 
	if #entry gt 0 then
		Append(~batch, entry);
	end if;
	if IsEof(s) then
		break;
	end if;
end while;

rules:=["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"];

count:=0;
for entry in batch do
	if &and[Regexp(rule, entry):rule in rules] then
		count+:=1;
	end if;
end for;
PrintFile("day04.txt",count);

function RuleCheck(document, ruleset)
	for rule in ruleset do
		bool, _, entry:=Regexp(rule*":([^ ]+)",document);
		if bool then
			entry:=entry[1];
			case rule:
				when "byr": 
					 if Regexp("[^0-9]",entry) then
					 	return false;
					 else
					 	n:=StringToInteger(entry);
					 	if n lt 1920 or n gt 2002 then
					 		return false;
					 	end if;
					 end if;
				when "iyr":
					if Regexp("[^0-9]",entry) then
					 	return false;
					 else
					 	n:=StringToInteger(entry);
					 	if n lt 2010 or n gt 2020 then
					 		return false;
					 	end if;
					 end if;
				when "eyr":
					if Regexp("[^0-9]",entry) then
					 	return false;
					 else
					 	n:=StringToInteger(entry);
					 	if n lt 2020 or n gt 2030 then
					 		return false;
					 	end if;
					 end if;
				when "hgt":
					check, ht:=Regexp("[0-9]+(in|cm)",entry);
					if check then
						h:=StringToInteger(Substring(ht, 1, #ht-2));
						u:=Substring(ht, #ht-1, 2);
						if u eq "in" then
							if h lt 59 or h gt 76 then
								return false;
							end if;
						elif u eq "cm" then
							if h lt 150 or h gt 193 then
								return false;
							end if;
						else
							return false;
						end if;
					else
						return false;
					end if;
				when "hcl":
					if not (#entry eq 7 and Regexp("#[0-9a-f]+",entry)) then
						return false;
					end if;
				when "ecl":
					if entry notin {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"} then
						return false;
					end if;
				when "pid":
					if not (#entry eq 9 and Regexp("[0-9]+",entry)) then
						return false;
					end if;
			end case;
		else
			return false;
		end if;
	end for;
	return true;
end function;

count:=0;
for doc in batch do
	if RuleCheck(doc, rules) then
		count+:=1;
	end if;
end for;
PrintFile("day04.txt",count);
