#include <iostream>
using namespace std;
int main(){
  string key1 = "Token 1";
  string key2 = "Token 2";
  string key3 = "Token 3";
  string key4 = "Token 4";
  string flag = "";
  for(int i = 0; i < key1.size();i++)
    if(key1.at(i) ==key2.at(i) && key1.at(i) == key3.at(i) && key1.at(i) == key4.at(i))
      flag+= key1.at(i);
  cout << flag << '\n';
}
