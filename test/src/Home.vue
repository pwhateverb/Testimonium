<template>
  <div id="app">
    <img id="logo" src="./assets/logo.png" />
    <div id="header">
      <p class="text-center sub-header">
        Testimonium is a platform that allows you to create and share your
        testimonies with the world.
      </p>
    </div>
    <button
      data-bs-toggle="modal"
      data-bs-target="#exampleModal"
      type="button"
      class="btn btn-outline-light txt_reqs"
    >
      Write<br />Requirements
    </button>
    <div
      class="modal fade"
      id="exampleModal"
      tabindex="-1"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">
              Write your requirements
            </h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <textarea
              v-model="requirements"
              style="height: 300px"
              class="form-control"
              aria-describedby="emailHelp"
            ></textarea>
          </div>
          <div
            class="modal-footer"
            style="display: inline-block; text-align: center"
          >
            <input
              type="file"
              id="fileUpload"
              accept=".pdf"
              style="display: none"
              @change="handleFileUpload"
            />

            <button
              @click="handleUpload()"
              type="button"
              class="btn btn-primary"
              style="width: 150px"
            >
              Upload
            </button>
          </div>
        </div>
      </div>
    </div>
    <div>
      <button
        @click="triggerFileUpload"
        type="button"
        class="btn btn-danger upload_pdf"
      >
        Upload PDF
      </button>
      <input
        type="file"
        ref="pdfUploader"
        @change="handleFileUpload"
        style="display: none"
        accept=".pdf"
      />
    </div>
    <div
      id="background"
      class="p-5 text-center bg-image"
      :style="{
        backgroundImage: `url(${backgroundImage})`,
      }"
    ></div>
    <div class="jumbotron">
      <h2 class="display-4">Product benefits</h2>
      <p class="lead">
        <br />Testamonium is a platform that allows you to fully automate the
        <br />process of writing detailed test specifcations from your
        requirements.
      </p>
      <hr class="my-4" />
      <img
        v-if="isLoading"
        src="./assets/loading.gif"
        alt="loading"
        id="loading"
      />
      <p>
        It uses utility classes for typography and spacing to space content out
        within the larger container.
      </p>
    </div>
  </div>
</template>
  
  <script>
import axios from "axios";
import { getDocument } from "pdfjs-dist/webpack";

export default {
  name: "home-page",
  data() {
    return {
      backgroundImage: require("@/assets/background.png"),
      isLoading: false,
      requirements: "",
    };
  },
  methods: {
    generate(requirements) {
      this.isLoading = true;
      const encodedRequirements = encodeURIComponent(requirements);
      axios
        .get("http://127.0.0.1:5000?requirements=" + encodedRequirements)
        .then((response) => {
          sessionStorage.setItem("tests", JSON.stringify(response.data));
          console.log("Tests:", sessionStorage.getItem("tests"));
          this.$router.push("/result");
        })
        .catch((error) => {
          console.error("Error making request:", error);
        });
    },
    triggerFileUpload() {
      this.$refs.pdfUploader.click();
      this.isLoading = true;
    },
    async handleFileUpload(event) {
      const file = event.target.files[0];
      if (file) {
        const message = await new Promise((resolve) => {
          const reader = new FileReader();
          reader.onload = async (e) => {
            const typedarray = new Uint8Array(e.target.result);
            const pdf = await getDocument(typedarray).promise;

            // Loop over all pages and extract text
            let text = "";
            for (let i = 1; i <= pdf.numPages; i++) {
              const page = await pdf.getPage(i);
              const textContent = await page.getTextContent();
              text += textContent.items.map((item) => item.str).join(" ");
            }

            resolve(text);
          };
          reader.readAsArrayBuffer(file);
        });

        console.log("Message:", message);
        this.generate(message);
      }
    },
    handleUpload() {
      const uploadedRequirements = this.requirements;
      this.generate(uploadedRequirements);
      this.requirements = "";
    },
  },
};
</script>
  
  <style>
#background {
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  height: 400px;
  width: 100%;
}

#logo {
  position: absolute;
  top: 13%;
  left: 40%;
  width: 340px;
  cursor: pointer;
}

#header {
  position: absolute;
  top: 20%;
  width: 100%;
}

.sub-header {
  color: rgb(234, 234, 234);
}

.txt_reqs {
  position: absolute;
  top: 230px;

  left: 44%;
  transform: translateX(-50%);
}

.upload_pdf {
  height: 60px;
  width: 125px;
  position: absolute;
  top: 230px;
  left: 56%;
  transform: translateX(-50%);
}

.jumbotron {
  background-color: #162a33;
  color: white;
  margin: 50px;
  padding: 10px;
}

#loading {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>
