<template>
  <div id="app">
    <div
      class="card"
      v-for="(fr, index) in functionalRequirements"
      :key="index"
      @click="toggleTestCases(fr.requirement_id)"
    >
      <h2>{{ fr.requirement_id }}</h2>
      <div class="test-cases" v-show="selectedFR === fr.requirement_id">
        <h3>Test Cases:</h3>
        <ul>
          <li
            v-for="(testCase, testCaseIndex) in fr.test_cases"
            :key="testCaseIndex"
          >
            <div class="test">
              <strong>Description:</strong> {{ testCase.description }}<br />
              <strong>Expected Result:</strong> {{ testCase.expected_result }}
            </div>
          </li>
        </ul>
      </div>
    </div>
    <div class="button" @click="downloadPDF()">
      <button type="button" class="btn btn-danger download_pdf">
        Download PDF
      </button>
    </div>
  </div>
</template>
<script>
import jsPDF from "jspdf";
export default {
  name: "result-page",
  data() {
    return {
      selectedFR: null,
      functionalRequirements: [],
    };
  },
  methods: {
    toggleTestCases(frKey) {
      this.selectedFR = this.selectedFR === frKey ? null : frKey;
    },
    downloadPDF() {
      const doc = new jsPDF();
      doc.setFontSize(12);
      var text = JSON.stringify(this.functionalRequirements, null, 2);
      var splitText = doc.splitTextToSize(text, 180);
      var y = 10;
      for (var i = 0, length = splitText.length; i < length; i++) {
        if (y > 280) {
          y = 10;
          doc.addPage();
        }
        y += 10;
        doc.text(splitText[i], 20, y);
      }
      doc.save("generated.pdf");
    },
  },
  mounted() {
    document.body.style.backgroundImage =
      "linear-gradient(to right, #696b6d, #3a6073)";
    let tests = sessionStorage.getItem("tests");
    console.log("T:", JSON.stringify(tests));
    if (typeof tests === "object") {
      this.functionalRequirements = tests.requirements;
    } else {
      this.functionalRequirements = JSON.parse(tests).requirements;
    }
  },
};
</script>

<style scoped>
.card {
  background-color: #162a33;
  color: white;
  margin: 50px;
  padding: 10px;
  cursor: pointer;
}
.test-cases {
  padding: 10px;
  border: 1px solid white;
  border-radius: 5px;
  margin-top: 10px;
}
.test {
  padding: 10px;
  border: 1px solid white;
  border-radius: 5px;
  margin-top: 10px;
}
.button {
  display: flex;
  justify-content: center;
  margin-bottom: 50px;
}
</style>