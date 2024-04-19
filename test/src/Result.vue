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
      functionalRequirements: {
        FR1: {
          description: "Plant Management",
          test_cases: [
            {
              description:
                "Verify that the user can view all plants in the system",
              expected_result:
                "All plants are displayed correctly in the plant management interface.",
            },
            {
              description: "Verify that the user can add a new plant",
              expected_result:
                "The new plant is successfully added to the database and displayed in the plant management interface.",
            },
            {
              description:
                "Verify that the user can update an existing plant's information",
              expected_result:
                "The updated information for the plant is saved to the database and displayed correctly in the plant management interface.",
            },
          ],
        },
        FR2: {
          description: "Notification System",
          test_cases: [
            {
              description:
                "Verify that the system does not send a notification when plant conditions are perfect",
              expected_result: "No notifications are sent to the user.",
            },
            {
              description:
                "Verify that the system sends a notification when moisture level is below threshold for a given plant",
              expected_result:
                "The user receives a notification about the low moisture level for the specified plant.",
            },
            {
              description:
                "Verify that the system sends a notification when temperature is above threshold for a given plant",
              expected_result:
                "The user receives a notification about the high temperature for the specified plant.",
            },
          ],
        },
        FR3: {
          description: "Notification System",
          test_cases: [
            {
              description:
                "Verify that the system does not send a notification when plant conditions are perfect",
              expected_result: "No notifications are sent to the user.",
            },
            {
              description:
                "Verify that the system sends a notification when moisture level is below threshold for a given plant",
              expected_result:
                "The user receives a notification about the low moisture level for the specified plant.",
            },
            {
              description:
                "Verify that the system sends a notification when temperature is above threshold for a given plant",
              expected_result:
                "The user receives a notification about the high temperature for the specified plant.",
            },
          ],
        },
        FR4: {
          description: "Notification System",
          test_cases: [
            {
              description:
                "Verify that the system does not send a notification when plant conditions are perfect",
              expected_result: "No notifications are sent to the user.",
            },
            {
              description:
                "Verify that the system sends a notification when moisture level is below threshold for a given plant",
              expected_result:
                "The user receives a notification about the low moisture level for the specified plant.",
            },
            {
              description:
                "Verify that the system sends a notification when temperature is above threshold for a given plant",
              expected_result:
                "The user receives a notification about the high temperature for the specified plant.",
            },
          ],
        },
        FR5: {
          description: "Notification System",
          test_cases: [
            {
              description:
                "Verify that the system does not send a notification when plant conditions are perfect",
              expected_result: "No notifications are sent to the user.",
            },
            {
              description:
                "Verify that the system sends a notification when moisture level is below threshold for a given plant",
              expected_result:
                "The user receives a notification about the low moisture level for the specified plant.",
            },
            {
              description:
                "Verify that the system sends a notification when temperature is above threshold for a given plant",
              expected_result:
                "The user receives a notification about the high temperature for the specified plant.",
            },
          ],
        },
        FR6: {
          description: "Notification System",
          test_cases: [
            {
              description:
                "Verify that the system does not send a notification when plant conditions are perfect",
              expected_result: "No notifications are sent to the user.",
            },
            {
              description:
                "Verify that the system sends a notification when moisture level is below threshold for a given plant",
              expected_result:
                "The user receives a notification about the low moisture level for the specified plant.",
            },
            {
              description:
                "Verify that the system sends a notification when temperature is above threshold for a given plant",
              expected_result:
                "The user receives a notification about the high temperature for the specified plant.",
            },
          ],
        },
        FR7: {
          description: "Notification System",
          test_cases: [
            {
              description:
                "Verify that the system does not send a notification when plant conditions are perfect",
              expected_result: "No notifications are sent to the user.",
            },
            {
              description:
                "Verify that the system sends a notification when moisture level is below threshold for a given plant",
              expected_result:
                "The user receives a notification about the low moisture level for the specified plant.",
            },
            {
              description:
                "Verify that the system sends a notification when temperature is above threshold for a given plant",
              expected_result:
                "The user receives a notification about the high temperature for the specified plant.",
            },
          ],
        },
      },
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