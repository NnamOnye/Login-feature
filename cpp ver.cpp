#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <unordered_map>


using namespace std;
//add users here or separate database
unordered_map<string, string> users = {
    {"user1", "123"},
    {"user2", "pass1"},
    {"user3", "pass2"}
};

bool login_if_statement()//IF-ELSE STATEMENT PRACTICE 
{
    //User Login Feature
    string user;
    string pass;

    cout << "Enter your username: ";
    cin >> user;
    if (users.find(user) != users.end()) {
        cout << "thank you! ";
    }
    else {
        cout << "Incorrect User." << endl;
        return false;
    }


    cout << "Enter your password:";
    cin >> pass;
    if (users[user] == pass) {
        cout << "Login successful!" << endl;
        return true;
    }
    else {
        cout << "Incorrect password." << endl;
        return false;
    }




}

int main()
{
    //call methods here to run code
    bool success = login_if_statement();
    return success ? 0 : 1;

}