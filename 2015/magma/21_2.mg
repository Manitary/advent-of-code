weapons:=[[8,4,0],[10,5,0],[25,6,0],[40,7,0],[74,8,0]];
armors:=[[13,0,1],[31,0,2],[31,0,2],[53,0,3],[75,0,4],[102,0,5]];
rings:=[[25,1,0],[50,2,0],[100,3,0],[20,0,1],[40,0,2],[80,0,3]];
boss:=[100,8,2];
max_gold:=0;
empty:=[0,0,0];
Append(~armors,empty);
Append(~rings,empty);
Append(~rings,empty);

procedure addstats(~stats,bonus)
	for i in [1..#bonus] do
		stats[i]+:=bonus[i];
	end for;
end procedure;

for weapon in weapons do
	for armor in armors do
		for r1 in [1..#rings-1] do
			for r2 in [r1+1..#rings] do
				stats:=[0,0,0];
				addstats(~stats,weapon);
				addstats(~stats,armor);
				addstats(~stats,rings[r1]);
				addstats(~stats,rings[r2]);
				if ((boss[1] div Maximum((stats[2]-boss[3]),1))+(boss[1] mod Maximum((stats[2]-boss[3]),1) eq 0 select 0 else 1)) gt ((100 div Maximum((boss[2]-stats[3]),1))+(100 mod Maximum((boss[2]-stats[3]),1) eq 0 select 0 else 1)) then
					max_gold:=Maximum(max_gold,stats[1]);
				end if;
			end for;
		end for;
	end for;
end for;
max_gold;