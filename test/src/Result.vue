<template>
  <div id="app">
    <div
      class="card"
      v-for="(fr, frKey) in functionalRequirements"
      :key="frKey"
      @click="toggleTestCases(frKey)"
    >
      <h2>{{ frKey }}</h2>
      <p>Description: {{ fr.description }}</p>
      <div class="test-cases" v-show="selectedFR === frKey">
        <h3>Test Cases:</h3>
        <ul>
          <li v-for="(testCase, index) in fr.test_cases" :key="index">
            <div class="test">
              <strong>Description:</strong> {{ testCase.description }}<br />
              <strong>Expected Result:</strong> {{ testCase.expected_result }}
            </div>
          </li>
        </ul>
      </div>
    </div>
    <div id="button" @click="downloadPDF()">
      <button type="button" class="btn btn-danger upload_pdf">
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
      functionalRequirements: process.env.TESTS,
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
#button {
  display: flex;
  justify-content: center;
  margin-bottom: 50px;
}
</style>