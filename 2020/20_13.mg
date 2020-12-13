F:=Open("input13.txt","r");
t:=StringToInteger(Gets(F));
input:=Split(Gets(F),",");
buses:=[StringToInteger(x):x in input|x ne "x"];
wait,id:=Min([bus*(t div bus + 1)-t:bus in buses]);
PrintFile("day13.txt",wait*buses[id]);
PrintFile("day13.txt",ChineseRemainderTheorem([1-Index(input,IntegerToString(bus)):bus in buses],buses));
