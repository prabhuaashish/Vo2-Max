<script>
    let raceTimeResult = null;
  
    async function calculateRaceTime() {
      // Get the values of the form fields by their IDs
      const frace = document.getElementById('frace').value;
      const r1 = document.getElementById('r1').value;
      const r1t_hours = document.getElementById('r1t_hours').value;
      const r1t_minutes = document.getElementById('r1t_minutes').value;
      const r1t_seconds = document.getElementById('r1t_seconds').value;
      const r2 = document.getElementById('r2').value;
      const r2t_hours = document.getElementById('r2t_hours').value;
      const r2t_minutes = document.getElementById('r2t_minutes').value;
      const r2t_seconds = document.getElementById('r2t_seconds').value;
      const mpw = document.getElementById('mpw').value;
      const dunits = document.getElementById('dunits').value;
  
      // Create the data object
      const data = {
        frace,
        r1,
        r1t_hours,
        r1t_minutes,
        r1t_seconds,
        mpw,
        dunits,
      };

      if (r2) {
        // Only include r2-related fields when r2 is not null
        data.r2 = r2;
        data.r2t_hours = r2t_hours;
        data.r2t_minutes = r2t_minutes;
        data.r2t_seconds = r2t_seconds;
      }
           
      // Send data to the server
      const response = await fetch('http://localhost:8000/calculate-race-time/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
      });
  
      if (response.ok) {
        const result = await response.json();
        raceTimeResult = result;
      }
    }
</script>
  
  
<div class="calc-outer-wrap">
    <h1>Race Time - Predictor</h1>
    <div id="form-error" style="display:none;"></div>
    <form class="calc-form" id="calc-form">
        <div class="form-fields">
          <div class="field-outer col-1">
              <label for="frace" class="top-label">Goal Race:</label>
              <div class="field-items">
                <div class="field field-large">
                    <select id="frace" name="frace">
                      <option selected="" value="marathon">Marathon</option>
                      <option value="half">Half Marathon</option>
                      <option value="10m">10 Miles</option>
                      <option value="10k">10K</option>
                      <option value="5m">5 Miles</option>
                      <option value="5k">5K</option>
                      <option value="3k">3K</option>
                      <option value="mile">1 Mile</option>
                      <option value="1500">1500 Meters</option>
                    </select>
                </div><!--  /.field -->
              </div><!--  /.field-items -->
          </div><!--  /.field-outer -->

          <div class="field-outer col-2">
              <label for="r1" class="top-label">Recent Race:</label>
              <div class="field-items">
                <div class="field field-large">
                    <select id="r1" name="r1">
                      <option value=""> </option>
                      <option value="marathon">Marathon</option>
                      <option value="half">Half Marathon</option>
                      <option value="10m">10 Miles</option>
                      <option value="10k">10K</option>
                      <option value="5m">5 Miles</option>
                      <option value="5k">5K</option>
                      <option value="3k">3K</option>
                      <option value="mile">1 Mile</option>
                      <option value="1500">1500 Meters</option>
                    </select>
                </div><!--  /.field -->
              </div><!--  /.field-items -->
          </div><!--  /.field-outer -->

          <div class="field-outer">
              <label for="r1t_hours" class="top-label"><span class="m-hide">Recent </span>Race Time:</label>
              <div class="field-items">
                <div class="field">
                    <input type="number" name="r1t_hours" id="r1t_hours" inputmode="numeric" pattern="[0-9]*" placeholder="Hour" maxlength="2">
                </div><!--  /.field -->
                <div class="field">
                    <input type="number" name="r1t_minutes" id="r1t_minutes" inputmode="numeric" pattern="[0-9]*" placeholder="Min" maxlength="2">
                </div><!--  /.field -->
                <div class="field">
                    <input type="number" name="r1t_seconds" id="r1t_seconds" inputmode="numeric" pattern="[0-9]*" placeholder="Sec" maxlength="2">
                </div><!--  /.field -->
              </div><!--  /.field-items -->
          </div><!--  /.field-outer -->

          <div class="field-outer col-2">
              <label for="r2" class="top-label">Another Race: <span class="small">(Optional)</span></label>
              <div class="field-items">
                <div class="field field-large">
                    <select id="r2" name="r2">
                      <option value=""> </option>
                      <option value="marathon">Marathon</option>
                      <option value="half">Half Marathon</option>
                      <option value="10m">10 Miles</option>
                      <option value="10k">10K</option>
                      <option value="5m">5 Miles</option>
                      <option value="5k">5K</option>
                      <option value="3k">3K</option>
                      <option value="mile">1 Mile</option>
                      <option value="1500">1500 Meters</option>
                    </select>
                </div><!--  /.field -->
              </div><!--  /.field-items -->
          </div><!--  /.field-outer -->

          <div class="field-outer">
              <label for="r2t_hours" class="top-label"><span class="m-hide">Another </span>Race Time: <span class="small">(Optional)</span></label>
              <div class="field-items">
                <div class="field">
                    <input type="number" name="r2t_hours" id="r2t_hours" inputmode="numeric" pattern="[0-9]*" placeholder="Hour" maxlength="2">
                </div><!--  /.field -->
                <div class="field">
                    <input type="number" name="r2t_minutes" id="r2t_minutes" inputmode="numeric" pattern="[0-9]*" placeholder="Min" maxlength="2">
                </div><!--  /.field -->
                <div class="field">
                    <input type="number" name="r2t_seconds" id="r2t_seconds" inputmode="numeric" pattern="[0-9]*" placeholder="Sec" maxlength="2">
                </div><!--  /.field -->
              </div><!--  /.field-items -->
          </div><!--  /.field-outer -->

          <div class="field-outer col-large">
              <label for="mpw" class="top-label">Mileage per week:</label>
              <div class="field-items">
                <div class="field">
                    <input type="number" name="mpw" id="mpw" inputmode="numeric" pattern="[0-9.]*">
                </div><!--  /.field -->

                <div class="field field-x-small">
                    <select name="dunits" id="dunits" class="unit">
                      <option value="mi">mi</option>
                      <option value="km">km</option>
                    </select>
                </div><!--  /.field-small -->
              </div><!--  /.field-items -->
          </div><!--  /.field-outer -->

          <div class="btn-wrap field-outer">
              <button on:click={calculateRaceTime} class="form-submit">Calculate</button>
          </div>
        </div><!--  /.form fields -->
    </form>
</div>
  
  
{#if raceTimeResult}
    <div class="result">
        <h2>Predicted Race Time: {raceTimeResult.predictedTime}</h2>
        <p>Pace per Mile: {raceTimeResult.paceMile}</p>
        <p>Pace per Kilometer: {raceTimeResult.paceKm}</p>
    </div>
{/if}

<style>
    .calc-outer-wrap {
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 20px;
    }
  
    .calc-form {
      width: 100%;
      max-width: 800px;
      background-color: #f2f2f2;
      border: 1px solid #ddd;
      border-radius: 5px;
      padding: 20px;
    }
  
    .form-fields {
      display: flex;
      flex-direction: column;
    }
  
    .field-outer {
      display: flex;
      flex-direction: column;
      margin-bottom: 10px;
    }
  
    .col-1 {
      width: 45%;
    }
  
    .col-2 {
      width: 45%;
    }
  
    .top-label {
      font-weight: bold;
      margin-bottom: 5px;
    }
  
    .field-items {
      display: flex;
      flex-direction: row;
    }
  
    .field {
      flex: 1;
      display: flex;
      flex-direction: column;
    }
  
    .field-large {
      width: 80%;
    }
  
    .field-x-small {
      width: 20%;
    }
  
    .unit {
      width: 100%;
    }
  
    .form-submit {
      background-color: #007bff;
      color: #fff;
      border: none;
      border-radius: 3px;
      padding: 10px 20px;
      margin-top: 10px;
      cursor: pointer;
    }
  
    .form-submit:hover {
      background-color: #0056b3;
    }
  
    .btn-wrap {
      align-items: center;
    }

    .result {
    background-color: #f5f5f5;
    padding: 15px;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin-top: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    }

    h2 {
        font-size: 24px;
        margin: 10px 0;
    }

    p {
        font-size: 18px;
        margin: 10px 0;
    }

</style>
  
  