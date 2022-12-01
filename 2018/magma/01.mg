nmod:=func<n,m|n mod m eq 0 select m else n mod m>;

F:=Open("input1.txt","r");
input:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~input,StringToInteger(s));
end while;

freq:=0;
freq_list:=[0];
sol2_found:=false;

for n in input do
	freq+:=n;
	if freq in freq_list then
		sol2:=freq;
		sol2_found:=true;
		shift:=&+input;
		break;
	end if;
	Append(~freq_list,freq);
end for;
shift:=freq;

PrintFile("day01.txt",shift);

if shift eq 0 then
	sol2:=0;
	sol2_found:=true;
end if;

if not(sol2_found) then
	modgroup:=[];
	for i in [2..#freq_list] do
		r:=nmod(freq_list[i],shift);
		if IsDefined(modgroup,r) then
			Append(~modgroup[r],<freq_list[i],i>);
		else
			modgroup[r]:=[<freq_list[i],i>];
		end if;
	end for;
	if shift gt 0 then
		modgroup:=[Sort(c):c in modgroup|#c gt 1];
	else
		modgroup:=[Reverse(Sort(c)):c in modgroup|#c gt 1];
	end if;
	gap:=(modgroup[1][2][1]-modgroup[1][1][1]) div shift;
	pos:=#input+1;
	for g in modgroup do
		for i in [1..#g-1] do
			gap_new:=(g[i+1][1]-g[i][1]) div shift;
			pos_new:=g[i][2];
			if gap_new lt gap then
				gap:=gap_new;
				pos:=pos_new;
				sol2:=g[i+1][1];
			elif gap_new eq gap and pos_new le pos then
				pos:=pos_new;
				sol2:=g[i+1][1];
			end if;
		end for;
	end for;
end if;

PrintFile("day01.txt",sol2);
