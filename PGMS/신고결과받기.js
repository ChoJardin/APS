function solution(id_list, report, k) {
    const answer = id_list.map(() => 0);

    const reportedBy = {};

    for (let i = 0; i < id_list.length; i++) {
        reportedBy[id_list[i]] = [];
    }

    // 신고한 사람 저장
    for (let i = 0; i < report.length; i++) {
        const [reporter, reported] = report[i].split(" ");

        // 이미 신고한 경우가 아니라면
        if (!reportedBy[reported].includes(reporter)) {
            reportedBy[reported].push(reporter);
        }
    }
    // 메일 발송
    for (let i = 0; i < id_list.length; i++) {
        const reported = id_list[i];
        if (reportedBy[reported].length >= k) {
            for (each of reportedBy[reported]) {
                answer[id_list.indexOf(each)] += 1;
            }
        }
    }

    return answer;
}
