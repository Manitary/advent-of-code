input:=[["set","i","31"],["set","a","1"],["mul","p","17"],["jgz","p","p"],["mul","a","2"],["add","i","-1"],["jgz","i","-2"],["add","a","-1"],["set","i","127"],["set","p","826"],["mul","p","8505"],["mod","p","a"],["mul","p","129749"],["add","p","12345"],["mod","p","a"],["set","b","p"],["mod","b","10000"],["snd","b"],["add","i","-1"],["jgz","i","-9"],["jgz","a","3"],["rcv","b"],["jgz","b","-1"],["set","f","0"],["set","i","126"],["rcv","a"],["rcv","b"],["set","p","a"],["mul","p","-1"],["add","p","b"],["jgz","p","4"],["snd","a"],["set","a","b"],["jgz","1","3"],["snd","b"],["set","f","1"],["add","i","-1"],["jgz","i","-11"],["snd","a"],["jgz","f","-16"],["jgz","a","-19"]];

//input:=[["snd","1"],["snd","2"],["snd","p"],["rcv","a"],["rcv","b"],["rcv","c"],["rcv","d"]];

function module(input,n)
	if input mod n eq 0 then
		return n;
	else
		return input mod n;
	end if;
end function;

function getvalue(string,registers,values)
	if string in registers then
		return values[Index(registers,string)];
	else
		return StringToInteger(string);
	end if;
end function;

procedure execute(id,input,~order_num,registers,~values,~queue,~waiting,~sent)
	order:=input[order_num[id]];
	case order[1]:
		when "snd":
			Append(~queue[3-id],getvalue(order[2],registers,values[id]));
			if id eq 2 then
				sent+:=1;
			end if;
		when "set":
			values[id][Index(registers,order[2])]:=getvalue(order[3],registers,values[id]);
		when "add":
			values[id][Index(registers,order[2])]+:=getvalue(order[3],registers,values[id]);
		when "mul":
			values[id][Index(registers,order[2])]*:=getvalue(order[3],registers,values[id]);
		when "mod":
			values[id][Index(registers,order[2])]mod:=getvalue(order[3],registers,values[id]);
		when "rcv":
			if #queue[id] gt 0 then
				waiting[id]:=false;
				values[id][Index(registers,order[2])]:=queue[id][1];
				Remove(~queue[id],1);
			else
				waiting[id]:=true;
				order_num[id]:=module(order_num[id]-1,#input);
			end if;
		when "jgz":
			if getvalue(order[2],registers,values[id]) gt 0 then
				order_num[id]+:=getvalue(order[3],registers,values[id])-1;
			end if;
	end case;
	order_num[id]:=module(order_num[id]+1,#input);
end procedure;

registers:={};
for item in input do
	bool,_,reg:=Regexp("([a-z]+)",item[2]);
	if bool then
		Include(~registers,reg[1]);
	end if;
end for;
registers:=SetToSequence(registers);
values:=[[0: register in registers] : i in [0..1]];
for i in [1..2] do
	values[i][Index(registers,"p")]:=i-1;
end for;
order_num:=[1,1];
waiting:=[false,false];
queue:=[[],[]];
sent:=0;

repeat
	id:=Random(1,2);
	execute(id,input,~order_num,registers,~values,~queue,~waiting,~sent);
until waiting eq [true,true] and queue eq [[],[]];
sent;