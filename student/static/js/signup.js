var nam=document.getElementById("name")
var email=document.getElementById("email")
var pass1=document.getElementById("pass1")
var pass2=document.getElementById("pass2")
var ph=document.getElementById("phno")

function validname(){
    var fn=nam.value;
    if (isNaN(fn)){
        nam.className="success";
        document.getElementById("text").innerHTML="";
    }else{
        nam.className="error";
        document.getElementById("signup").disabled=true;
        document.getElementById("text").innerHTML="Please enter name";
    }
}

function validemail(){
    var mail=email.value;
   
    var re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,3}$/;
    if (re.test(mail)){
        email.className="success";
        document.getElementById("text").innerHTML="";
    }else{
        email.className="error";
        document.getElementById("signup").disabled=true;
        document.getElementById("text").innerHTML="Please enter valid email";
    }
}

function validph(){
    var num=phno.value
    if (isNaN(num)){
        phno.className="error";
        document.getElementById("signup").disabled=true;
        document.getElementById("text").innerHTML="Please enter valid phone number";
    }else{
        var numl=num.length
        if (numl==10){
            phno.className="success";
            document.getElementById("text").innerHTML="";
        }else{
            phno.className="error";
            document.getElementById("signup").disabled=true;
            document.getElementById("text").innerHTML="Please enter valid phone number";
        }
        
    }
}

function validpass(){
    var passl = pass1.value.length;
    if (passl >=8 & passl <=16){
        pass1.className="success";
        document.getElementById("text").innerHTML ="";
    }else{
        pass1.className ="error";
        document.getElementById("signup").disabled=true;
        document.getElementById("text").innerHTML="Password length must be greater than 8 character  and not excced 15";
    }
}

function validpassconform(){
    var pass =pass1.value;
    var passc =pass2.value;
    if (pass == passc){
        pass2.className = "success";
        document.getElementById("text").innerHTML="";
        document.getElementById("signup").disabled=false;
    }else{
        document.getElementById("signup").disabled=true;
        pass2.className="error";
        document.getElementById("text").innerHTML="Password not match";
    }
}