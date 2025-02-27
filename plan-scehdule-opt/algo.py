import os
import json
import nextroute
import nextmv
import nextmv.cloud

class DecisionModel(nextmv.Model):
    def solve(self, input: nextmv.Input) -> nextmv.Output:
        """Solves the given problem and returns the solution."""

        nextroute_input = nextroute.schema.Input.from_dict(input.data)
        nextroute_options = nextroute.Options.extract_from_dict(input.options.to_dict())
        nextroute_output = nextroute.solve(nextroute_input, nextroute_options)

        return nextmv.Output(
            options=input.options,
            solution=nextroute_output.solutions[0].to_dict(),
            statistics=nextroute_output.statistics.to_dict(),
        )
    
parameters = []

default_options = nextroute.Options()
for name, default_value in default_options.to_dict().items():
    parameters.append(nextmv.Parameter(name.lower(), type(default_value), default_value, name, False))

options = nextmv.Options(*parameters)

model = DecisionModel()

sample_input = {
  "defaults": {
    "vehicles": {
      "capacity": {
        "bunnies": 20,
        "rabbits": 10
      },
      "start_location": {
        "lat": 35.791729813680874,
        "lon": -78.7401685145487
      },
      "end_location": {
        "lat": 35.791729813680874,
        "lon": -78.7401685145487
      },
      "speed": 10
    },
    "stops": {
      "duration": 300,
      "quantity": {
        "bunnies": -1,
        "rabbits": -1
      },
      "unplanned_penalty": 200000,
      "target_arrival_time": "2023-01-01T10:00:00Z",
      "early_arrival_time_penalty": 1.5,
      "late_arrival_time_penalty": 1.5
    }
  },
  "stops": [
    {
      "id": "s1",
      "location": {
        "lon": -78.90919,
        "lat": 35.72389
      },
      "compatibility_attributes": ["premium"]
    },
    {
      "id": "s2",
      "location": {
        "lon": -78.813862,
        "lat": 35.75712
      },
      "compatibility_attributes": ["premium"]
    },
    {
      "id": "s3",
      "location": {
        "lon": -78.92996,
        "lat": 35.932795
      },
      "compatibility_attributes": ["premium"]
    },
    {
      "id": "s4",
      "location": {
        "lon": -78.505745,
        "lat": 35.77772
      },
      "compatibility_attributes": ["premium"]
    },
    {
      "id": "s5",
      "location": {
        "lon": -78.75084,
        "lat": 35.732995
      },
      "compatibility_attributes": ["premium"]
    },
    {
      "id": "s6",
      "location": {
        "lon": -78.788025,
        "lat": 35.813025
      },
      "compatibility_attributes": ["premium"]
    },
    {
      "id": "s7",
      "location": {
        "lon": -78.749391,
        "lat": 35.74261
      },
      "compatibility_attributes": ["premium"]
    },
    {
      "id": "s8",
      "location": {
        "lon": -78.94658,
        "lat": 36.039135
      },
      "compatibility_attributes": ["basic"]
    },
    {
      "id": "s9",
      "location": {
        "lon": -78.64972,
        "lat": 35.64796
      },
      "compatibility_attributes": ["basic"]
    },
    {
      "id": "s10",
      "location": {
        "lon": -78.747955,
        "lat": 35.672955
      },
      "compatibility_attributes": ["basic"]
    },
    {
      "id": "s11",
      "location": {
        "lon": -78.83403,
        "lat": 35.77013
      },
      "compatibility_attributes": ["basic"]
    },
    {
      "id": "s12",
      "location": {
        "lon": -78.864465,
        "lat": 35.782855
      },
      "compatibility_attributes": ["basic"]
    },
    {
      "id": "s13",
      "location": {
        "lon": -78.952142,
        "lat": 35.88029
      },
      "compatibility_attributes": ["basic"]
    },
    {
      "id": "s14",
      "location": {
        "lon": -78.52748,
        "lat": 35.961465
      },
      "compatibility_attributes": ["basic"]
    },
    {
      "id": "s15",
      "location": {
        "lon": -78.89832,
        "lat": 35.83202
      }
    },
    {
      "id": "s16",
      "location": {
        "lon": -78.63216,
        "lat": 35.83458
      }
    },
    {
      "id": "s17",
      "location": {
        "lon": -78.76063,
        "lat": 35.67337
      }
    },
    {
      "id": "s18",
      "location": {
        "lon": -78.911485,
        "lat": 36.009015
      }
    },
    {
      "id": "s19",
      "location": {
        "lon": -78.522705,
        "lat": 35.93663
      }
    },
    {
      "id": "s20",
      "location": {
        "lon": -78.995162,
        "lat": 35.97414
      }
    },
    {
      "id": "s21",
      "location": {
        "lon": -78.50509,
        "lat": 35.7606
      }
    },
    {
      "id": "s22",
      "location": {
        "lon": -78.828547,
        "lat": 35.962635
      },
      "precedes": ["s16", "s23"]
    },
    {
      "id": "s23",
      "location": {
        "lon": -78.60914,
        "lat": 35.84616
      },
      "start_time_window": [
        "2023-01-01T09:00:00-06:00",
        "2023-01-01T09:30:00-06:00"
      ]
    },
    {
      "id": "s24",
      "location": {
        "lon": -78.65521,
        "lat": 35.740605
      },
      "start_time_window": [
        "2023-01-01T09:00:00-06:00",
        "2023-01-01T09:30:00-06:00"
      ],
      "succeeds": "s25"
    },
    {
      "id": "s25",
      "location": {
        "lon": -78.92051,
        "lat": 35.887575
      },
      "start_time_window": [
        "2023-01-01T09:00:00-06:00",
        "2023-01-01T09:30:00-06:00"
      ],
      "precedes": "s26"
    },
    {
      "id": "s26",
      "location": {
        "lon": -78.84058,
        "lat": 35.823865
      },
      "start_time_window": [
        "2023-01-01T09:00:00-06:00",
        "2023-01-01T09:30:00-06:00"
      ]
    }
  ],
  "vehicles": [
    {
      "id": "vehicle-0",
      "start_time": "2023-01-01T06:00:00-06:00",
      "end_time": "2023-01-01T10:00:00-06:00",
      "activation_penalty": 4000,
      "compatibility_attributes": ["premium"]
    },
    {
      "id": "vehicle-1",
      "start_time": "2023-01-01T10:00:00-06:00",
      "end_time": "2023-01-01T16:00:00-06:00",
      "max_duration": 21000,
      "compatibility_attributes": ["basic"]
    }
  ]
}


input = nextmv.Input(data=sample_input, options=options)
output = model.solve(input)
print(json.dumps(output.solution, indent=2))