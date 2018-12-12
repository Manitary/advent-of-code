F:=Open("input12.txt","r");
_,plants,_:=Regexp("([.#])+",Gets(F));
Gets(F);
pre:=[];
post:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	_,_,r:=Regexp("([.#]+) => ([.#])",s);
	Append(~pre,r[1]);
	Append(~post,r[2]);
end while;
m:=map<pre->post|x:->post[Index(pre,x)]>;

procedure adjust(~p,~i)
	l:=5;
	i1:=Index(p,"#");
	if i1 lt l then
		p:=&*[".":i in [1..l-i1]]*p;
	elif i1 gt l then
		p:=Substring(p,i1-l+1,#p-i1+l);
	end if;
	i+:=l-i1;
	i2:=Index(Reverse(p),"#");
	if i2 lt l then
		p*:=&*[".":i in [1..l-i2]];
	elif i2 gt l then
		p:=Substring(p,1,#p-i2+l);
	end if;
end procedure;

function evolve(p)
	return &*[i gt 2 and i lt #p-1 select m(&*[p[j]:j in [i-2..i+2]]) else p[i]:i in [1..#p]];
end function;

function pots(p,i)
	return &+{*j-i:j in [1..#p]|p[j] eq "#"*};
end function;

patterns:=[];
stored_idx:=[];

n:=5*10^10;
idx:=1;
adjust(~plants,~idx);

for k in [1..n] do
	plants:=evolve(plants);
	adjust(~plants,~idx);
	if k eq 20 then
		PrintFile("day12.txt",pots(plants,idx));
	end if;
	if plants notin patterns then
		Append(~patterns,plants);
		Append(~stored_idx,idx);
	else
		first:=Index(patterns,plants);
		l:=k-first;
		diff_idx:=stored_idx[first]-idx;
		break;
	end if;
end for;

num_loops:=(n-first+1) div l;
last:=n-first+1-l*num_loops;
base:=last eq 0 select first else first+last-1;

PrintFile("day12.txt",pots(patterns[base],stored_idx[base])+(num_loops-1)*diff_idx*Multiplicity(Eltseq(patterns[base]),"#"));
