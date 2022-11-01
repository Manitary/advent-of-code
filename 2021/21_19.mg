F:=Open("input19.txt","r");

scanners:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	if Regexp("scanner", s) then
		Append(~scanners, []);
	elif #s eq 0 then
		continue;
	else
		Append(~scanners[#scanners], Vector([StringToInteger(x):x in Split(s, ",")]));
	end if;
end while;

m1:=Matrix([[1,0,0],[0,0,-1],[0,1,0]]);
m2:=Matrix([[0,0,1],[0,1,0],[-1,0,0]]);
m3:=Matrix([[0,-1,0],[1,0,0],[0,0,1]]);
rotations:=MatrixGroup<SL(3,Integers())|m1,m2,m3>;

scan_done:={1};
scan_id:={2..#scanners};
coords:=[Vector([0,0,0])];

repeat
	for i in scan_id do
		for j in scan_done do
			for r in rotations do
				beacons:=[x*r:x in scanners[i]];
				for b1 in beacons, b2 in scanners[j] do
					v:=b2-b1;
					tbeacons:=[x+v:x in beacons];
					if #(SequenceToSet(scanners[j]) meet SequenceToSet(tbeacons)) ge 12 then
						coords[i]:=Vector([0,0,0])+v;
						scanners[i]:=tbeacons;
						Include(~scan_done,i);
						Exclude(~scan_id,i);
						break j;
					end if;
				end for;
			end for;
		end for;
	end for;
until #scan_id eq 0;

numbeacons:=#&join{SequenceToSet(x):x in scanners};
maxdist:=Max([Abs(p[1]-q[1])+Abs(p[2]-q[2])+Abs(p[3]-q[3]):p,q in coords|p ne q]);

PrintFile("day19.txt",numbeacons);
PrintFile("day19.txt",maxdist);
