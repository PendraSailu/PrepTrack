document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("quiz-form");

    if (!form) {
        return;
    }

    const panels = Array.from(
        document.querySelectorAll(".question-panel")
    );

    const jumpButtons = Array.from(
        document.querySelectorAll(".question-jump")
    );

    const timerElement = document.getElementById("quiz-timer");
    const counterElement = document.getElementById("question-counter");
    const answeredElement = document.getElementById("answered-counter");
    const progressElement = document.getElementById("quiz-progress");
    const previousButton = document.getElementById("previous-button");
    const nextButton = document.getElementById("next-button");
    const submitButton = document.getElementById("submit-button");
    const messageElement = document.getElementById("quiz-message");

    const totalQuestions = panels.length;
    const duration = Number(form.dataset.duration) || 300;

    let currentQuestion = 0;
    let submitted = false;
    let deadline = Date.now() + duration * 1000;
    let timerInterval = null;

    if (totalQuestions === 0) {
        return;
    }

    function getAnsweredCount() {
        return panels.filter(function (panel) {
            return panel.querySelector('input[type="radio"]:checked');
        }).length;
    }

    function updateAnswerStyles() {
        panels.forEach(function (panel) {
            const options = panel.querySelectorAll("[data-option-label]");

            options.forEach(function (label) {
                const input = label.querySelector("input");

                label.classList.toggle(
                    "selected",
                    Boolean(input && input.checked)
                );
            });
        });
    }

    function updateNavigation() {
        panels.forEach(function (panel, index) {
            panel.hidden = index !== currentQuestion;
        });

        jumpButtons.forEach(function (button, index) {
            const panel = panels[index];
            const answered = Boolean(
                panel.querySelector('input[type="radio"]:checked')
            );

            button.classList.toggle("current", index === currentQuestion);
            button.classList.toggle("answered", answered);
        });

        counterElement.textContent =
            "Question " + (currentQuestion + 1) + " of " + totalQuestions;

        const answeredCount = getAnsweredCount();

        answeredElement.textContent = "Answered: " + answeredCount;

        progressElement.style.width =
            ((currentQuestion + 1) / totalQuestions * 100) + "%";

        previousButton.disabled = currentQuestion === 0;

        nextButton.hidden = currentQuestion === totalQuestions - 1;
        submitButton.hidden = currentQuestion !== totalQuestions - 1;

        messageElement.textContent = "";
        updateAnswerStyles();
    }

    function showQuestion(index) {
        if (index < 0 || index >= totalQuestions) {
            return;
        }

        currentQuestion = index;
        updateNavigation();
    }

    function submitQuiz(automatically = false) {
        if (submitted) {
            return;
        }

        if (!automatically) {
            const unanswered = totalQuestions - getAnsweredCount();

            let message = "Are you sure you want to submit your quiz?";

            if (unanswered > 0) {
                message =
                    "You have " + unanswered +
                    " unanswered question(s). Submit anyway?";
            }

            if (!window.confirm(message)) {
                return;
            }
        }

        submitted = true;

        if (timerInterval !== null) {
            clearInterval(timerInterval);
        }

        submitButton.disabled = true;
        submitButton.textContent = automatically
            ? "Time is up. Submitting..."
            : "Submitting...";

        // Use the native form submission method.
        HTMLFormElement.prototype.submit.call(form);
    }

    function updateTimer() {
        if (submitted) {
            return;
        }

        const remaining = Math.max(
            0,
            Math.ceil((deadline - Date.now()) / 1000)
        );

        const minutes = Math.floor(remaining / 60);
        const seconds = remaining % 60;

        timerElement.textContent =
            String(minutes).padStart(2, "0") + ":" +
            String(seconds).padStart(2, "0");

        if (remaining <= 60) {
            timerElement.classList.add("timer-warning");
        } else {
            timerElement.classList.remove("timer-warning");
        }

        if (remaining <= 0) {
            clearInterval(timerInterval);
            submitQuiz(true);
        }
    }

    previousButton.addEventListener("click", function () {
        showQuestion(currentQuestion - 1);
    });

    nextButton.addEventListener("click", function () {
        showQuestion(currentQuestion + 1);
    });

    jumpButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            showQuestion(Number(button.dataset.jump));
        });
    });

    form.addEventListener("change", function (event) {
        if (event.target.matches('input[type="radio"]')) {
            updateNavigation();
        }
    });

    form.addEventListener("submit", function (event) {
        if (submitted) {
            return;
        }

        event.preventDefault();
        submitQuiz(false);
    });

    // Set up the interval before the first timer update.
    timerInterval = setInterval(updateTimer, 250);

    updateNavigation();
    updateTimer();
});