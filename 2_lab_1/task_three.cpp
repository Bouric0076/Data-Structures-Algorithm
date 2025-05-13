#include <iostream>
using namespace std;

class Course {
public:
    string course_code, course_name;
};

class Grade {
public:
    int mark;
    char the_grade;

    void calculateGrade() {
        if (mark > 69) the_grade = 'A';
        else if (mark > 59) the_grade = 'B';
        else if (mark > 49) the_grade = 'C';
        else if (mark > 39) the_grade = 'D';
        else the_grade = 'E';
    }
};

class Student {
private:
    bool gradeFinalized = false;
public:
    string reg_no, name;
    int age;
    Course course;
    Grade grade;

    void inputDetails() {
        cout << "Enter registration number: ";
        cin >> reg_no;
        cin.ignore();
        cout << "Enter name: ";
        getline(cin, name);
        cout << "Enter age: ";
        cin >> age;
        cin.ignore();
        cout << "Enter course code: ";
        getline(cin, course.course_code);
        cout << "Enter course name: ";
        getline(cin, course.course_name);
    }

    void updateMarks() {
        if (gradeFinalized) {
            cout << "Grade already finalized.\n";
            return;
        }
        cout << "Enter marks: ";
        cin >> grade.mark;
        grade.calculateGrade();
        gradeFinalized = true;
        cout << "Grade: " << grade.the_grade << endl;
    }

    void displayDetails() {
        cout << "Registration Number: " << reg_no << endl;
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
        cout << "Course Code: " << course.course_code << endl;
        cout << "Course Name: " << course.course_name << endl;
        cout << "Marks: " << grade.mark << endl;
        cout << "Grade: " << grade.the_grade << endl;
    }
};

