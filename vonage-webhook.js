export default function handler(req, res) {
  if (req.method === 'POST' || req.method === 'GET') {
    const ncco = [
      {
        "action": "talk",
        "text": "Empire AI dispatch. Do you need roof repair, water removal, or tree clearing? Tell me now, or press 1 for roof, 2 for water, 3 for trees.",
        "voiceName": "Joey", 
        "bargeIn": true
      },
      {
        "action": "input",
        "type": [ "speech", "dtmf" ],
        "dtmf": {
          "maxDigits": 1,
          "timeOut": 15
        },
        "speech": {
          "endOnSilence": 2,
          "language": "en-US",
          "timeOut": 15
        },
        "eventUrl": ["https://your-vercel-app.vercel.app/api/route-lead"]
      }
    ];
    res.status(200).json(ncco);
  } else {
    res.status(405).send('Method Not Allowed');
  }
}
