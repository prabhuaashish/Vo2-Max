<script>
    import Button from '../../lib/components/Button.svelte';

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
      const response = await fetch('http://localhost:8000/calculate/race-time/', {
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
                      <option value="half_marathon">Half Marathon</option>
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
                    <select required id="r1" name="r1">
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
                    <input type="text" name="r1t_hours" id="r1t_hours" inputmode="numeric" pattern="[0-9]*" placeholder="Hr" maxlength="2">
                </div><!--  /.field -->
                <div class="field">
                    <input type="text" name="r1t_minutes" id="r1t_minutes" inputmode="numeric" pattern="[0-9]*" placeholder="Min" maxlength="2">
                </div><!--  /.field -->
                <div class="field">
                    <input type="text" name="r1t_seconds" id="r1t_seconds" inputmode="numeric" pattern="[0-9]*" placeholder="Sec" maxlength="2">
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
                    <input type="text" name="r2t_hours" id="r2t_hours" inputmode="numeric" pattern="[0-9]*" placeholder="Hr" maxlength="2">
                </div><!--  /.field -->
                <div class="field">
                    <input type="text" name="r2t_minutes" id="r2t_minutes" inputmode="numeric" pattern="[0-9]*" placeholder="Min" maxlength="2">
                </div><!--  /.field -->
                <div class="field">
                    <input type="text" name="r2t_seconds" id="r2t_seconds" inputmode="numeric" pattern="[0-9]*" placeholder="Sec" maxlength="2">
                </div><!--  /.field -->
              </div><!--  /.field-items -->
          </div><!--  /.field-outer -->

          <div class="field-outer col-large">
              <label for="mpw" class="top-label">Mileage per week:</label>
              <div class="field-items">
                <div class="field">
                    <input required type="text" name="mpw" id="mpw" inputmode="numeric" pattern="[0-9.]*">
                </div><!--  /.field -->

                <div class="field field-x-small">
                    <select name="dunits" id="dunits" class="unit">
                      <option value="mi">mi</option>
                      <option value="km">km</option>
                    </select>
                </div><!--  /.field-small -->
              </div><!--  /.field-items -->
          </div><!--  /.field-outer -->
        </div><!--  /.form fields -->

        <div class="btn-wrap field-outer">
          <Button on:click={calculateRaceTime}>Calculate</Button>
        </div>
    </form>
</div>
  
  
{#if raceTimeResult}
    <div class="result">
        <h2>Predicted Race Time: {raceTimeResult.predictedTime}</h2>
        <p>Pace per Mile: {raceTimeResult.paceMile}</p>
        <p>Pace per Kilometer: {raceTimeResult.paceKm}</p>
    </div>
{/if}

<style lang="scss">
    .calc-outer-wrap {
        max-width: 700px;
        margin: 0 auto;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
  
    h1 {
        text-align: center;
        font-size: 24px;
        margin-bottom: 20px;
        @include breakpoint.down('md') {
            font-size: 20px;
        }
    }
  
    .form-fields {
        display: flex;
        flex-direction: column;
        margin-bottom: 10px;
    }
  
    .field-outer {
      display: flex;
      flex-direction: column;
      margin-bottom: 10px;
    }

    .field-outer input {
        width: 100%;
        display: flex;;
    }
  
    .top-label {
      font-weight: bold;
      margin-bottom: 3px;
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
  
    .field-x-small select {
      width: 50%;      
    }
  
    .btn-wrap {
      align-items: center;
    }

    .result {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      margin-top: 20px;
      display: flex;
      flex-direction: column;
    }

    h2 {
        font-size: 24px;
        margin: 10px 0;

        @include breakpoint.down('md') {
            font-size: 16px;
        }
    }

    p {
        font-size: 18px;
        margin: 10px 0;

        @include breakpoint.down('md') {
            font-size: 16px;
        }
    }
    
    select {
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    input[type="text"] {
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

</style>
  
  