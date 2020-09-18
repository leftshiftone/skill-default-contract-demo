# skill-default-contract-demo

Demonstrates how to implement a contract provided by leftshift one.

All default contracts are open source and can be found [here](https://github.com/leftshiftone/skill-contracts)

In this example we implement a very simple tokenizer that implementes the [leftshiftone/tokenizer](https://github.com/leftshiftone/skill-contracts/blob/master/src/main/resources/leftshiftone/tokenizer/schema.dbs) default contract:

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

