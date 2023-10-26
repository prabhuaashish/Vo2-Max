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
        r2,
        r2t_hours,
        r2t_minutes,
        r2t_seconds,
        mpw,
        dunits,
      };
  
    console.log(data);
         
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
            <input type="text" name="r1t_hours" id="r1t_hours" inputmode="numeric" pattern="[0-9]*" placeholder="Hour">
        </div><!--  /.field -->
        <div class="field">
            <input type="text" name="r1t_minutes" id="r1t_minutes" inputmode="numeric" pattern="[0-9]*" placeholder="Min">
        </div><!--  /.field -->
        <div class="field">
            <input type="text" name="r1t_seconds" id="r1t_seconds" inputmode="numeric" pattern="[0-9]*" placeholder="Sec">
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
            <input type="text" name="r2t_hours" id="r2t_hours" inputmode="numeric" pattern="[0-9]*" placeholder="Hour">
        </div><!--  /.field -->
        <div class="field">
            <input type="text" name="r2t_minutes" id="r2t_minutes" inputmode="numeric" pattern="[0-9]*" placeholder="Min">
        </div><!--  /.field -->
        <div class="field">
            <input type="text" name="r2t_seconds" id="r2t_seconds" inputmode="numeric" pattern="[0-9]*" placeholder="Sec">
        </div><!--  /.field -->
        </div><!--  /.field-items -->
    </div><!--  /.field-outer -->

    <div class="field-outer col-large">
        <label for="mpw" class="top-label">Mi/Km run per week:</label>
        <div class="field-items">
        <div class="field">
            <input type="text" name="mpw" id="mpw" inputmode="numeric" pattern="[0-9.]*">
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
<div>
    <h2>Predicted Race Time: {raceTimeResult.predictedTime}</h2>
    <p>Pace per Mile: {raceTimeResult.paceMile}</p>
    <p>Pace per Kilometer: {raceTimeResult.paceKm}</p>
</div>
{/if}

<style lang="scss">
    @media (min-width: 22.5rem){
        .calc-outer-wrap {
        padding: 0.625rem;
        }  
    }
    .calc-outer-wrap {
    margin: 0 auto;
    background: #f3f3f3;
    font-size: 1rem;
    line-height: 1.3;
    font-family: Helvetica Neue, Helvetica, Arial, sans-serif;
    padding: 0 0.625rem;
    }

    * {
    box-sizing: border-box;
    }

    div {
    display: block;
    }

    #form-error {
    color: #fff;
    margin-bottom: 0.5rem;
    text-align: center;
    color: #c1000b;
    background-color: #ffd5d5;
    padding: 3px;
    font-size: 0.875rem;
    }

    form {
    display: block;
    margin-top: 0em;
    }

    .form-fields {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: flex-end;
    }

    @media (min-width: 45rem){
        .field-outer {
            width: 48%;
            flex-basis: calc(50% - 10px);
            margin-bottom: 5px;
        }
    }

    .field-large {
    flex: 1;
    width: 67%;
    }

    select {
    font-size: 0.875rem;
    }

    input, select {
    height: 1.75rem;
    border: 1px solid #bbb;
    width: 100%;
    background: #fff;
    padding: 0 0.325rem;
    border-radius: 0.1875rem;
    transition: box-shadow 200ms ease-in-out;
    box-shadow: inset 0 0 0 0 #59e7ed;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    }

    label, input, select {
    font-size: 1em;
    line-height: 1.3;
    display: block;
    }

    select:not(:-internal-list-box) {
    background-color: buttonface;
    overflow: visible !important;
    }

    option {
    font-weight: normal;
    display: block;
    white-space-collapse: collapse;
    text-wrap: nowrap;
    min-height: 1.2em;
    padding: 0px 2px 1px;
    }

    .top-label {
    font-weight: bold;
    font-size: 0.875rem;
    line-height: 1.4;
    display: block;
    }

    .field-items {
    display: flex;
    justify-content: space-between;
    }
    .field-large {
    flex: 1;
    width: 67%;
    }

    @media (min-width: 45rem){
        .field-outer {
            width: 48%;
            flex-basis: calc(50% - 10px);
            margin-bottom: 5px;
        }
    }

    .field-outer {
    width: 32%;
    flex-basis: calc(100% / 3 - 5px);
    }

    @media (min-width: 45rem) {
        .m-hide {
            display: inline;
        }
    }

    .m-hide {
    display: none;
    }

    .field + .field {
    margin-left: 3px;
    }

    .field {
    display: inline-block;
    width: 32%;
    flex-grow: 1;
    }


    .btn-wrap {
    align-self: flex-end;
    margin: 5px 0 0 auto;
    margin-left: auto;
    flex-basis: 12rem;
    }

    .form-submit {
    background: #59e7ed;
    display: block;
    border: 0;
    width: 100%;
    font-size: 1rem;
    border-radius: 0.1875rem;
    height: 1.5rem;
    color: #fff;
    box-shadow: 1px 1px 1px 0 rgba(0, 0, 0, 0.15);
    cursor: pointer;
    text-transform: uppercase;
    }

</style>