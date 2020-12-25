F:=Open("input20.txt","r");

tile:=AssociativeArray();
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	if "T" in s then
		_, n:=Regexp("[0-9]+",s);
		grid:=[];
	elif #s gt 0 then
		Append(~grid,s);
	elif #s eq 0 then
		tile[StringToInteger(n)]:=grid;
	end if;
end while;
id:=Keys(tile);
l:=#tile[Random(id)];
dim:=Integers()!SquareRoot(#id);

function printgrid(x)
	out:="";
	for i in [1..l] do
		out*:=tile[x][i];
		out*:="\n";
	end for;
	return out;
end function;

function borders(tile);
	return [[tile[1,i]:i in [1..l]], [tile[i,l]:i in [1..l]], [tile[l,i]:i in [1..l]], [tile[i,1]:i in [1..l]]];
end function;

function rotate(grid,i)
	if i eq 1 then
		return [[grid[a,b]:a in [#grid..1 by -1]]:b in [1..#grid]];
	elif i gt 1 then
		return rotate(rotate(grid,i-1),1);
	end if;
end function;

function flip(grid)
	return [Reverse(r):r in grid];
end function;

function allimages(grid)
	list:=[];
	for i in [1..4] do
		Append(~list,rotate(grid,i));
		Append(~list,flip(rotate(grid,i)));
	end for;
	return list;
end function;

border:=AssociativeArray();
for k in id do
	tile[k]:=allimages(tile[k]);
	border[k]:=[borders(x):x in tile[k]];
end for;

function index(x,y)
	return (y-1)*dim+x;
end function;

function findpic(picture, x, y, seen)
	if y gt dim then
		return true, picture;
	end if;
	x1:=x+1;
	y1:=y;
	if x1 gt dim then
		x1:=1;
		y1+:=1;
	end if;
	for k in id do
		if k in seen then
			continue;
		end if;
		seen1:=Include(seen,k);
		for i in [1..8] do
			if x gt 1 then
				if border[picture[index(x-1,y)][1],picture[index(x-1,y)][2]][2] ne border[k][i][4] then
					continue;
				end if;
			end if;
			if y gt 1 then
				if border[picture[index(x,y-1)][1],picture[index(x,y-1)][2]][3] ne border[k][i][1] then
					continue;
				end if;
			end if;
			bool, pic:=findpic(Append(picture,[k,i]),x1,y1,seen1);
			if bool then
				return true, pic;
			end if;
		Exclude(~seen1,k);
		end for;
	end for;
	return false, _;
end function;

_, list:=findpic([],1,1,{});

sol:=&*[list[index(x,y),1]:x in [1,12], y in [1,12]];

picture:=[];
for y in [1..dim] do
	for i in [2..l-1] do
		Append(~picture,[]);
		for x in [1..dim] do
			picture[#picture] cat:= [tile[list[index(x,y)][1]][list[index(x,y)][2]][i][j]:j in [2..l-1]];
		end for;
	end for;
end for;

function printpic(pic)
	str:="";
	for i in [1..#pic] do
		str *:= &*pic[i];
		str *:= "\n";
	end for;
	return str;
end function;

monster:="                  # 
#    ##    ##    ###
 #  #  #  #  #  #   ";
monster:=[Eltseq(x):x in Split(monster,"\n")];

allpics:=allimages(picture);

for pic in allpics do
	print "pic #:", Index(allpics,pic);
	count:=0;
	for y in [1..#pic-#monster+1], x in [1..#pic-#monster[1]+1] do
		for j in [1..#monster], i in [1..#monster[1]] do
			if monster[j,i] eq "#" and pic[y+j-1,x+i-1] ne "#" then
				continue x;
			end if;
		end for;
		count+:=1;
	end for;
	if count ne 0 then
		break;
	end if;
end for;

n:=0;
for r in picture, c in r do 
	if c eq "#" then
		n+:=1;
	end if;
end for;

m:=0;
for r in monster, c in r do
	if c eq "#" then
		m+:=1;
	end if;
end for;

PrintFile("day20.txt",sol);
PrintFile("day20.txt",n-m*count);
