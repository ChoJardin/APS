function solution(new_id) {
    var answer = "";
    answer = new_id.toLowerCase();
    answer.replace(/[~!@#$%^&*()=+[{\]}:?,<>]/, "");
    answer.replace(/[..]/, ".");
    answer = answer.endsWith(".") ? answer.slice(0, -1) : answer;
    answer = answer.startsWith(".") ? answer.slice(1) : answer;
    answer = answer === "" ? (answer = "a") : answer;
    answer = answer.length > 16 ? answer.slice(0, 14) : answer;
    answer = answer.endsWith(".") ? answer.slice(0, -1) : answer;

    answer = answer.slice(-1, -2);

    return answer;
}

console.log(solution("...!@BaT#*..y.abcdefghijklm"));
