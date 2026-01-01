const ALGO_COMPLEXITY = {
    bubble: { best: "O(n)", average: "O(n²)", worst: "O(n²)", space: "O(1)", stable: "Yes" },
    selection: { best: "O(n²)", average: "O(n²)", worst: "O(n²)", space: "O(1)", stable: "No" },
    insertion: { best: "O(n)", average: "O(n²)", worst: "O(n²)", space: "O(1)", stable: "Yes" },
    merge: { best: "O(n log n)", average: "O(n log n)", worst: "O(n log n)", space: "O(n)", stable: "Yes" },
    quick: { best: "O(n log n)", average: "O(n log n)", worst: "O(n²)", space: "O(log n)", stable: "No" },
    heap: { best: "O(n log n)", average: "O(n log n)", worst: "O(n log n)", space: "O(1)", stable: "No" }
};

function estimateBigO(algo, n) {
    switch (algo) {
        case "bubble":
        case "selection":
        case "insertion":
            return n * n;
        case "merge":
        case "heap":
        case "quick":
            return n * Math.log2(n);
        default:
            return n;
    }
}

let baseArray = [];
let speed = 60;

const containerA = document.getElementById("containerA");
const containerB = document.getElementById("containerB");

document.getElementById("generate").addEventListener("click", generateArray);
document.getElementById("start").addEventListener("click", compareAlgorithms);

function renderArray(container, arr, highlight = [], type = "") {
    container.innerHTML = "";
    const maxVal = Math.max(...arr);

    arr.forEach((value, index) => {
        const lane = document.createElement("div");
        lane.classList.add("lane");
        lane.style.width = `${(value / maxVal) * 100}%`;

        if (highlight.includes(index)) {
            lane.classList.add(type);
        }

        container.appendChild(lane);
    });
}

function updateComplexity(algo, id) {
    const c = ALGO_COMPLEXITY[algo];
    document.getElementById(id).innerHTML = `
        <p><strong>Best:</strong> ${c.best}</p>
        <p><strong>Average:</strong> ${c.average}</p>
        <p><strong>Worst:</strong> ${c.worst}</p>
        <p><strong>Space:</strong> ${c.space}</p>
        <p><strong>Stable:</strong> ${c.stable}</p>
    `;
}

async function generateArray() {
    const size = document.getElementById("size").value;
    const res = await fetch(`/api/random?size=${size}`);
    baseArray = await res.json();

    renderArray(containerA, baseArray);
    renderArray(containerB, baseArray);
}

async function compareAlgorithms() {
    speed = document.getElementById("speed").value;

    const algoA = document.getElementById("algorithmA").value;
    const algoB = document.getElementById("algorithmB").value;

    updateComplexity(algoA, "complexityA");
    updateComplexity(algoB, "complexityB");

    const [resA, resB] = await Promise.all([
        fetch("/api/sort", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ algorithm: algoA, array: [...baseArray] })
        }).then(r => r.json()),

        fetch("/api/sort", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ algorithm: algoB, array: [...baseArray] })
        }).then(r => r.json())
    ]);

    animate(resA, containerA, algoA, "A");
    animate(resB, containerB, algoB, "B");
}

async function animate(result, container, algo, suffix) {
    for (const step of result.steps) {
        renderArray(container, step.array, step.compare || [], step.swap ? "swap" : "compare");
        await sleep(speed);
    }

    const comparisons = result.stats.comparisons;
    const swaps = result.stats.swaps;
    const totalSteps = comparisons + swaps;
    const n = result.steps[0].array.length;
    const expected = estimateBigO(algo, n);

    document.getElementById(`comp${suffix}`).textContent = `Comparisons: ${comparisons}`;
    document.getElementById(`swap${suffix}`).textContent = `Swaps: ${swaps}`;
    document.getElementById(`steps${suffix}`).textContent = `Total Steps: ${totalSteps}`;

    const maxScale = Math.max(totalSteps, expected);
    document.getElementById(`actual${suffix}`).style.width = `${(totalSteps / maxScale) * 100}%`;
    document.getElementById(`expected${suffix}`).style.left = `${(expected / maxScale) * 100}%`;
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

generateArray();
