# skill-default-contract-demo

Demonstrates how to implement a contract provided by leftshift one.

All default contracts are open source and can be found [here](https://github.com/leftshiftone/skill-contracts/tree/master/src/main/resources/leftshiftone)

Default contracts specify how a skill solving a specific kind of business problem can be used by a client. Since some
parts of AIOS are using default skill implementations provided by leftshift one this implementations may be replaced
by implementations provided by the users of AIOS if the implementation adheres to the said default contract.

This example implements a very simple tokenizer that fulfils the [leftshiftone/tokenizer](https://github.com/leftshiftone/skill-contracts/blob/master/src/main/resources/leftshiftone/tokenizer/schema.dbs) default contract:

```
namespace incoming {
    class Request {
        text: string
    }
}

namespace outgoing {
    class Response {
      tokens: [string]
    }
}
```

### Implementing a default contract

In order to implement a default contract the contract to be implemented must be defined within the `skill.yml` file
in the format `leftshiftone/CONTRACT` where all available contracts can be found [here](https://github.com/leftshiftone/skill-contracts/tree/master/src/main/resources/leftshiftone).
So to implement the tokenizer default contract the `skill.yml` file must be adapted as following:

```yaml
...
contract: ["leftshiftone/tokenizer"]
...
```

This means that that skill implements the default `leftshiftone/tokenizer` ([Definition](https://github.com/leftshiftone/skill-contracts/blob/master/src/main/resources/leftshiftone/tokenizer/schema.dbs)) contract. It is possible to implement more than
one contract (default and/or custom). 

### Using custom contracts

Of course we can not anticipate every business problem so custom contracts may be defined by the skill developer. 
Custom contracts are defined by creating one (or more) contracts using the [Dynabuffers IDL](https://github.com/leftshiftone/dynabuffers). Default contracts must be
placed at a well defined location within the skills project structure.

**Python:** `src/contract/`


**WARN:** Using `incoming` and `outgoing` namespaces is a convention that must be followed!

A contract for a rather trivial addition only calculator could look like this:
```
namespace incoming {
    class CalculatorRequest {
        x: int
        y: int
    }
}

namespace outgoing {
    class CalculatorResponse {
      result: int
    }
}
```

If only a single contract is implemented a root level namespace can be omitted.