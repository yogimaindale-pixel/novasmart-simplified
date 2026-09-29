# 🏛️ 10. Senior Principal Engineer Guide & Extension Architecture

### Extending NovaSmart with New Tools (e.g. Order Status Tool)
1. Add `query_order_status(db_conn, order_id)` function.
2. Register function in `NovaSmartAgent.tools['query_order_status']`.
3. Connect tool outputs to A2UI card renderer in `a2ui_utils.py`.
