document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".quiz").forEach(function (quiz) {
    const feedback = quiz.querySelector(".fb");
    quiz.querySelectorAll(".opts button").forEach(function (btn) {
      btn.addEventListener("click", function () {
        const ok = btn.dataset.correct === "1";
        btn.classList.add(ok ? "correct" : "wrong");
        quiz.querySelectorAll(".opts button").forEach(function (b) {
          b.disabled = true;
          if (b.dataset.correct === "1" && !ok) b.classList.add("correct");
        });
        feedback.textContent = ok ? quiz.dataset.ok : quiz.dataset.no;
      });
    });
  });
});
