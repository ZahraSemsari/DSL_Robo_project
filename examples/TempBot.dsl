robot TempBot {
  sensors {
    sensor temperature: float;
  }

  actuators {
    actuator heater: Heater;
  }

  vars {
    var target: float = 30.0;
  }

  behavior TempControl {
    initial Idle;

    state Idle {
      update_on {
        if (temperature < target) goto Heating;
      }
    }

    state Heating {
      enter_on {
        heater.on();
      }

      update_on {
        if (temperature >= target) goto Idle;
      }

      exit_on {
        heater.off();
      }
    }
  }
}
